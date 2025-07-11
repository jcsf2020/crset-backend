#!/bin/bash

echo "🔧 [1/9] Limpar ambiente antigo..."
docker stop financeflow-backend 2>/dev/null
docker rm financeflow-backend 2>/dev/null
docker rmi financeflow-backend 2>/dev/null

echo "📦 [2/9] Instalar dependências (se necessário)..."
pip install fastapi uvicorn python-dotenv stripe

echo "🧠 [3/9] Validar se \'checkout_session.py\' está na pasta \'routes\' e tem router configurado..."
ROUTES_FILE="./routes/checkout_session.py"
if [ ! -f "$ROUTES_FILE" ]; then
  echo "❌ ERRO: Ficheiro $ROUTES_FILE não encontrado. Corrige e volta a correr."
  exit 1
fi

if ! grep -q "APIRouter" "$ROUTES_FILE"; then
  echo "❌ ERRO: Ficheiro $ROUTES_FILE não define um \'router = APIRouter()\'."
  exit 1
fi

echo "✅ routes/checkout_session.py validado."

echo "🧠 [4/9] Corrigir imports em main.py se necessário..."
MAIN_FILE="main.py"

# Remove any previous problematic lines added by the script
sed -i "/from routes.checkout_session import router as checkout_router/d" "$MAIN_FILE"
sed -i "/app.include_router(checkout_router, prefix=\'\/\')/d" "$MAIN_FILE"
sed -i "/app.include_router(checkout_router, prefix=\'\')/d" "$MAIN_FILE"

# Ensure the correct import and include lines are present
if ! grep -q "from routes.checkout_session import router" "$MAIN_FILE"; then
  sed -i "1i from routes.checkout_session import router" "$MAIN_FILE"
fi

if ! grep -q "app.include_router(router, prefix=\"\", tags=\"[Checkout\"])" "$MAIN_FILE"; then
  # This assumes the line 'app = FastAPI()' exists and we want to add after it
  sed -i "/app = FastAPI()/a\app.include_router(router, prefix=\"\", tags=[\"Checkout\"])" "$MAIN_FILE"
fi

echo "✅ Import e include verificados/adicionados a main.py"

echo "🐳 [5/9] Construir imagem Docker..."
docker build -t financeflow-backend .

if [ $? -ne 0 ]; then
  echo "❌ ERRO ao buildar imagem Docker. Verifica o Dockerfile."
  exit 1
fi

echo "🚀 [6/9] Correr o container na porta 8000..."
docker run -d --name financeflow-backend -p 8000:8000 financeflow-backend

echo "⏳ A aguardar o arranque do backend..."
sleep 5

echo "🔍 [7/9] Testar se a rota está ativa com curl..."
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/create-checkout-session -X POST -H "Content-Type: application/json" -d "{}")

if [ "$RESPONSE" == "200" ]; then
  echo "✅ API a responder corretamente com status 200 OK"
else
  echo "❌ ERRO: API respondeu com código $RESPONSE"
  echo "Sugestão: Verifica se a função em \'checkout_session.py\' está com \'@router.post(\'/create-checkout-session\')\'."
fi

echo "📂 [8/9] Listar estrutura de ficheiros relevante:"
ls -R

echo "🎯 [9/9] Docker Logs recentes:"
docker logs financeflow-backend --tail 20


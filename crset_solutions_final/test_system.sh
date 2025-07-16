#!/bin/bash

echo "🚀 CRSET Solutions - Teste do Sistema"
echo "====================================="

# Verificar se Docker está a correr
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker não está a correr. Por favor, inicia o Docker primeiro."
    exit 1
fi

echo "✅ Docker está ativo"

# Parar containers existentes
echo "🛑 A parar containers existentes..."
docker compose down --volumes --remove-orphans

# Construir e iniciar
echo "🔨 A construir e iniciar containers..."
docker compose up --build -d

# Aguardar que os serviços estejam prontos
echo "⏳ A aguardar que os serviços estejam prontos..."
sleep 30

# Testar backend
echo "🧪 A testar backend..."
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo "✅ Backend está funcional"
else
    echo "❌ Backend não está a responder"
fi

# Testar frontend
echo "🧪 A testar frontend..."
if curl -f http://localhost:3000 > /dev/null 2>&1; then
    echo "✅ Frontend está funcional"
else
    echo "❌ Frontend não está a responder"
fi

echo ""
echo "🎉 Sistema testado! Acede a:"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:8000"
echo "   Swagger Docs: http://localhost:8000/docs"
echo ""
echo "Para parar: docker compose down"

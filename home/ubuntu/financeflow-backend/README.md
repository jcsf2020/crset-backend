# FinanceFlow Backend - Docker Ready (Rebuild)

Este projeto é um backend FastAPI para processar pagamentos Stripe, permitindo a criação de sessões de checkout.

## 🚀 Estado Atual e Como Executar

O backend foi validado e está funcional, pronto para ser executado em containers Docker. O endpoint de criação de sessão de checkout Stripe (`/create-checkout-session`) está a responder, mas requer chaves de API Stripe válidas para gerar um URL de checkout real.

### Pré-requisitos
- Docker instalado e funcional
- Uma API Key Stripe (testável ou real)

### Configuração

1. **Navegue para o diretório do projeto:**
   ```bash
   cd financeflow-backend
   ```

2. **Configure as variáveis de ambiente:**
   O ficheiro `.env` já está incluído no projeto com chaves de teste. **Para que o checkout Stripe funcione, você DEVE substituir estas chaves pelas suas chaves Stripe válidas.**
   ```
   STRIPE_SECRET_KEY=sk_test_SUA_CHAVE_SECRETA_AQUI
   STRIPE_PUBLISHABLE_KEY=pk_test_SUA_CHAVE_PUBLIC_AQUI
   ```

3. **Construa a imagem Docker:**
   ```bash
   docker build -t financeflow-backend .
   ```

4. **Corra o container Docker:**
   ```bash
   docker run -d --name financeflow-backend --env-file .env -p 8000:8000 financeflow-backend
   ```

### Testar o Backend

1. **Verificar se o backend está ativo (endpoint raiz):**
   ```bash
   curl http://localhost:8000
   ```
   Deverá ver a resposta: `{"message":"Backend ativo"}`

2. **Testar o endpoint de criação de sessão de checkout Stripe:**
   ```bash
   curl -X POST http://localhost:8000/create-checkout-session -H "Content-Type: application/json" -d '{"price": 9.99}'
   ```
   Se as suas chaves Stripe estiverem configuradas corretamente, a resposta incluirá um URL de checkout do Stripe. Caso contrário, receberá um erro de chave inválida, como `{"error":"Invalid API Key provided: ..."}`.

## 📂 Estrutura do Projeto

```
financeflow-backend/
├── main.py
├── routes/
│   └── checkout_session.py
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

## 🧪 Debug Rápido

- **`curl: (7) Failed to connect`**: O container pode não estar a correr ou a porta não está exposta corretamente. Verifique `docker ps` e os logs do container (`docker logs financeflow-backend`).
- **`{"detail":"Not Found"}` no endpoint raiz**: O endpoint raiz (`/`) foi adicionado e testado. Se vir este erro, certifique-se de que o `main.py` está atualizado e a imagem Docker foi reconstruída.
- **`{"error":"Invalid API Key provided: ..."}`**: As chaves Stripe no seu ficheiro `.env` são inválidas ou não estão configuradas corretamente. Substitua-as pelas suas chaves válidas.

## 📝 Notas Finais

O projeto foi reconstruído e validado para garantir a sua funcionalidade. O problema de `NameError` e o erro de prefixo do router foram resolvidos. O backend está agora pronto para ser utilizado com as suas chaves Stripe reais para um checkout funcional.


# 🚀 CRSET Solutions - Sistema Completo

Sistema completo de gestão de serviços e contactos para CRSET Solutions, com backend FastAPI, frontend Next.js e base de dados PostgreSQL.

## ✅ Funcionalidades

- **Backend FastAPI** com autenticação JWT
- **Frontend Next.js** responsivo com Tailwind CSS
- **Base de dados PostgreSQL** com Docker
- **CRUD completo de serviços**
- **Sistema de contactos** com integração Resend
- **Autenticação e autorização**
- **API documentada** com Swagger
- **Docker Compose** para desenvolvimento

## 🚀 Início Rápido

### 1. Clonar e configurar

```bash
# Copiar variáveis de ambiente
cp .env.example .env

# Editar .env com as tuas chaves (opcional para desenvolvimento)
```

### 2. Executar com Docker

```bash
# Subir todos os serviços
docker compose up --build

# Ou em background
docker compose up --build -d
```

### 3. Aceder às aplicações

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432

## 📊 Endpoints da API

### Autenticação
- `POST /api/auth/register` - Registar utilizador
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Perfil do utilizador

### Serviços
- `GET /api/services/` - Listar serviços
- `POST /api/services/` - Criar serviço (autenticado)
- `PUT /api/services/{id}` - Atualizar serviço (autenticado)
- `DELETE /api/services/{id}` - Eliminar serviço (autenticado)

### Contactos
- `POST /api/contacts/` - Criar contacto
- `GET /api/contacts/` - Listar contactos (autenticado)

## 🔧 Desenvolvimento

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```

## 🌐 Deploy

### Railway (Backend)
1. Conectar repositório ao Railway
2. Configurar variáveis de ambiente
3. Deploy automático

### Vercel (Frontend)
1. Conectar repositório ao Vercel
2. Configurar `NEXT_PUBLIC_API_URL`
3. Deploy automático

## 📧 Configuração de Email

Para ativar o envio de emails via Resend:

1. Criar conta em https://resend.com
2. Obter API key
3. Configurar `RESEND_API_KEY` no .env
4. Verificar domínio (opcional)

## 🔐 Variáveis de Ambiente

Consultar `.env.example` para todas as variáveis disponíveis.

## 📱 Contactos

- **Email**: crsetsolutions@gmail.com
- **Telefone**: +351 914 423 688
- **Localização**: Vila Nova de Gaia, Portugal

---

**Desenvolvido por CRSET Solutions** 🚀

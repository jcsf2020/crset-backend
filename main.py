
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import logging
from dotenv import load_dotenv
from datetime import datetime
import uvicorn

# Importar routers
from routers import dashboard, assets, opportunities, simulator, exports, mascots, auth

# Carregar variáveis de ambiente
load_dotenv()

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Criar aplicação FastAPI
app = FastAPI(
    title="Finance Flow Personal API",
    description="API de gestão financeira pessoal para João Fonseca - CRSET Solutions",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "https://*.abacusai.app",
        os.getenv("FRONTEND_URL", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(assets.router, prefix="/api/assets", tags=["Assets"])
app.include_router(opportunities.router, prefix="/api/opportunities", tags=["Opportunities"])
app.include_router(simulator.router, prefix="/api/simulator", tags=["Simulator"])
app.include_router(exports.router, prefix="/api/exports", tags=["Exports"])
app.include_router(mascots.router, prefix="/api/mascots", tags=["Mascots"])

@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {
        "message": "Finance Flow Personal API",
        "version": "1.0.0",
        "user": "João Fonseca",
        "timestamp": datetime.now().isoformat(),
        "status": "operational",
        "endpoints": {
            "dashboard": "/api/dashboard",
            "assets": "/api/assets",
            "opportunities": "/api/opportunities", 
            "simulator": "/api/simulator",
            "exports": "/api/exports",
            "mascots": "/api/mascots",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Finance Flow Personal API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "database": "connected",
        "user": "João Fonseca"
    }

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Handler global para exceções"""
    logger.error(f"Global exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Erro interno do servidor",
            "message": "Algo deu errado. Tente novamente.",
            "timestamp": datetime.now().isoformat()
        }
    )

if __name__ == "__main__":
    port = int(os.getenv("API_PORT", 8001))
    host = os.getenv("API_HOST", "0.0.0.0")
    debug = os.getenv("DEBUG", "false").lower() == "true"
    
    logger.info(f"Starting Finance Flow Personal API on {host}:{port}")
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug,
        log_level="info"
    )


from fastapi import APIRouter, HTTPException, Depends
from models import SuccessResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/me")
async def get_current_user():
    """Obter dados do utilizador atual (João Fonseca)"""
    return {
        "id": "joao-fonseca-001",
        "name": "João Fonseca",
        "email": "joao.fonseca@crset.com",
        "phone": "+351 914 423 688",
        "role": "owner",
        "company": "CRSET Solutions"
    }

@router.post("/login")
async def login():
    """Login simplificado para uso pessoal"""
    return {
        "access_token": "personal-access-token",
        "token_type": "bearer",
        "user": {
            "name": "João Fonseca",
            "email": "joao.fonseca@crset.com"
        }
    }

@router.post("/register")
async def register():
    """Registo simplificado para uso pessoal"""
    return {
        "message": "Utilizador registado com sucesso",
        "user": {
            "name": "João Fonseca",
            "email": "joao.fonseca@crset.com",
            "id": "joao-fonseca-001"
        }
    }

@router.post("/logout")
async def logout():
    """Logout"""
    return SuccessResponse(message="Logout realizado com sucesso")

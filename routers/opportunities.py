
from fastapi import APIRouter, HTTPException, Depends
from models import OpportunityCreate, OpportunityUpdate, OpportunityResponse, SuccessResponse
from database import get_db
from typing import List, Optional
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/", response_model=List[OpportunityResponse])
async def get_opportunities(
    status: Optional[str] = None,
    type: Optional[str] = None,
    priority: Optional[str] = None
):
    """Obter lista de oportunidades"""
    try:
        # Simular dados das oportunidades (em produção seriam queries reais)
        opportunities = [
            # Oportunidades abertas
            {
                "id": "opp-001",
                "title": "Apartamento T2 no Porto",
                "description": "Imobiliário para arrendamento, ROI estimado 8%/ano",
                "type": "REAL_ESTATE",
                "status": "OPEN",
                "value": 120000.0,
                "priority": "HIGH",
                "deadline": "2025-08-15T00:00:00Z",
                "contact": "Maria Silva - Remax",
                "notes": "Zona em valorização, perto do metro",
                "tags": ["imobiliario", "rendimento", "porto"],
                "createdAt": "2025-06-15T00:00:00Z",
                "updatedAt": "2025-07-07T00:00:00Z"
            },
            {
                "id": "opp-002",
                "title": "Startup FinTech - Série A",
                "description": "Investimento em startup de pagamentos digitais",
                "type": "INVESTMENT", 
                "status": "IN_PROGRESS",
                "value": 25000.0,
                "priority": "MEDIUM",
                "deadline": "2025-07-30T00:00:00Z",
                "contact": "Pedro Santos - CEO",
                "notes": "Due diligence em curso, equipa forte",
                "tags": ["startup", "fintech", "serie-a"],
                "createdAt": "2025-06-01T00:00:00Z",
                "updatedAt": "2025-07-05T00:00:00Z"
            },
            {
                "id": "opp-003",
                "title": "Solana Staking Pool",
                "description": "Participação em pool de staking, 6% APY",
                "type": "CRYPTO",
                "status": "OPEN", 
                "value": 5000.0,
                "priority": "LOW",
                "deadline": None,
                "contact": "DeFi Protocol",
                "notes": "Baixo risco, rendimento passivo",
                "tags": ["solana", "staking", "defi"],
                "createdAt": "2025-06-20T00:00:00Z",
                "updatedAt": "2025-07-02T00:00:00Z"
            },
            {
                "id": "opp-004",
                "title": "Parceria CRSET x TechCorp",
                "description": "Joint venture para projetos de IA",
                "type": "PARTNERSHIP",
                "status": "OPEN",
                "value": 50000.0,
                "priority": "HIGH",
                "deadline": "2025-09-01T00:00:00Z",
                "contact": "Ana Costa - TechCorp",
                "notes": "Potencial de 3x em 2 anos",
                "tags": ["partnership", "ai", "techcorp"],
                "createdAt": "2025-06-10T00:00:00Z",
                "updatedAt": "2025-07-06T00:00:00Z"
            },
            # Oportunidades fechadas esta semana (sucesso)
            {
                "id": "opp-005",
                "title": "Consultoria Bancária Digital",
                "description": "Projeto de transformação digital 3 meses",
                "type": "PROJECT",
                "status": "CLOSED_WON",
                "value": 18000.0,
                "priority": "HIGH",
                "deadline": None,
                "contact": "Millennium BCP",
                "notes": "Fechado na segunda-feira, excelente margem",
                "tags": ["consultoria", "bancario", "digital"],
                "createdAt": "2025-06-15T00:00:00Z",
                "updatedAt": "2025-07-07T00:00:00Z"
            },
            {
                "id": "opp-006",
                "title": "Workshop Empresas Tech",
                "description": "Formação em estratégia financeira para startups",
                "type": "PROJECT",
                "status": "CLOSED_WON",
                "value": 8500.0,
                "priority": "MEDIUM",
                "deadline": None,
                "contact": "Tech Hub Lisboa", 
                "notes": "Fechado na quarta-feira, 2 workshops",
                "tags": ["formacao", "startups", "workshop"],
                "createdAt": "2025-06-25T00:00:00Z",
                "updatedAt": "2025-07-05T00:00:00Z"
            },
            {
                "id": "opp-007",
                "title": "Assessoria Investimento Particular",
                "description": "Gestão de portfólio para cliente VIP",
                "type": "INVESTMENT",
                "status": "CLOSED_WON",
                "value": 12000.0,
                "priority": "HIGH", 
                "deadline": None,
                "contact": "Cliente VIP",
                "notes": "Fechado ontem, contrato anual",
                "tags": ["assessoria", "vip", "portfolio"],
                "createdAt": "2025-06-28T00:00:00Z",
                "updatedAt": "2025-07-06T00:00:00Z"
            }
        ]

        # Aplicar filtros
        if status:
            opportunities = [opp for opp in opportunities if opp["status"] == status.upper()]
        if type:
            opportunities = [opp for opp in opportunities if opp["type"] == type.upper()]
        if priority:
            opportunities = [opp for opp in opportunities if opp["priority"] == priority.upper()]

        return opportunities

    except Exception as e:
        logger.error(f"Error getting opportunities: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter oportunidades")

@router.get("/{opportunity_id}", response_model=OpportunityResponse)
async def get_opportunity(opportunity_id: str):
    """Obter oportunidade específica"""
    mock_opportunity = {
        "id": opportunity_id,
        "title": "Apartamento T2 no Porto",
        "description": "Imobiliário para arrendamento, ROI estimado 8%/ano",
        "type": "REAL_ESTATE",
        "status": "OPEN",
        "value": 120000.0,
        "priority": "HIGH",
        "deadline": "2025-08-15T00:00:00Z",
        "contact": "Maria Silva - Remax",
        "notes": "Zona em valorização, perto do metro",
        "tags": ["imobiliario", "rendimento", "porto"],
        "createdAt": "2025-06-15T00:00:00Z",
        "updatedAt": "2025-07-07T00:00:00Z"
    }
    return mock_opportunity

@router.post("/", response_model=OpportunityResponse)
async def create_opportunity(opportunity: OpportunityCreate):
    """Criar nova oportunidade"""
    try:
        new_opportunity = {
            "id": f"opp-new-{opportunity.title.lower().replace(' ', '-')[:10]}",
            "title": opportunity.title,
            "description": opportunity.description,
            "type": opportunity.type,
            "status": opportunity.status,
            "value": opportunity.value,
            "priority": opportunity.priority,
            "deadline": opportunity.deadline.isoformat() if opportunity.deadline else None,
            "contact": opportunity.contact,
            "notes": opportunity.notes,
            "tags": opportunity.tags,
            "createdAt": "2025-07-07T00:00:00Z",
            "updatedAt": "2025-07-07T00:00:00Z"
        }

        logger.info(f"Opportunity created: {new_opportunity['title']}")
        return new_opportunity

    except Exception as e:
        logger.error(f"Error creating opportunity: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao criar oportunidade")

@router.put("/{opportunity_id}", response_model=OpportunityResponse)
async def update_opportunity(opportunity_id: str, opportunity: OpportunityUpdate):
    """Atualizar oportunidade existente"""
    try:
        updated_opportunity = {
            "id": opportunity_id,
            "title": opportunity.title or "Apartamento T2 no Porto",
            "description": opportunity.description or "Imobiliário para arrendamento",
            "type": opportunity.type or "REAL_ESTATE",
            "status": opportunity.status or "OPEN",
            "value": opportunity.value or 120000.0,
            "priority": opportunity.priority or "HIGH",
            "deadline": opportunity.deadline.isoformat() if opportunity.deadline else "2025-08-15T00:00:00Z",
            "contact": opportunity.contact or "Maria Silva - Remax",
            "notes": opportunity.notes or "Zona em valorização",
            "tags": opportunity.tags or ["imobiliario", "rendimento"],
            "createdAt": "2025-06-15T00:00:00Z",
            "updatedAt": "2025-07-07T00:00:00Z"
        }

        logger.info(f"Opportunity updated: {opportunity_id}")
        return updated_opportunity

    except Exception as e:
        logger.error(f"Error updating opportunity: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar oportunidade")

@router.delete("/{opportunity_id}")
async def delete_opportunity(opportunity_id: str):
    """Eliminar oportunidade"""
    try:
        logger.info(f"Opportunity deleted: {opportunity_id}")
        return SuccessResponse(message=f"Oportunidade {opportunity_id} eliminada com sucesso")

    except Exception as e:
        logger.error(f"Error deleting opportunity: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao eliminar oportunidade")

@router.get("/summary/stats")
async def get_opportunities_summary():
    """Obter resumo das oportunidades"""
    return {
        "total": 11,
        "open": 8,
        "inProgress": 1,
        "closedWon": 3,
        "closedLost": 0,
        "onHold": 0,
        "weeklyRevenue": 38500.0,  # 3 leads fechadas esta semana
        "averageValue": 34545.45,
        "totalPipeline": 200000.0,
        "byType": {
            "REAL_ESTATE": 2,
            "INVESTMENT": 3,
            "PROJECT": 3,
            "PARTNERSHIP": 1,
            "CRYPTO": 1,
            "BUSINESS": 1
        },
        "byPriority": {
            "HIGH": 5,
            "MEDIUM": 4,
            "LOW": 2
        }
    }

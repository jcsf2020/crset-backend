
from fastapi import APIRouter, HTTPException
from models import MascotResponse, MascotMessage, MascotContextData, Priority
import logging
import random
from datetime import datetime

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/")
async def get_mascots():
    """Obter lista de mascotes CRSET"""
    try:
        mascots = [
            {
                "id": "mascot-boris",
                "name": "Boris",
                "personality": "Conservador e analítico. Especialista em gestão de risco.",
                "avatar": "https://images.unsplash.com/photo-1517849845537-4d257902454a?w=200",
                "isActive": True,
                "currentMessage": None
            },
            {
                "id": "mascot-laya",
                "name": "Laya", 
                "personality": "Otimista e inovadora. Focada em oportunidades de crescimento.",
                "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200",
                "isActive": True,
                "currentMessage": None
            },
            {
                "id": "mascot-irina",
                "name": "Irina",
                "personality": "Equilibrada e estratégica. Especialista em diversificação.",
                "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200",
                "isActive": True,
                "currentMessage": None
            }
        ]

        return {"mascots": mascots}

    except Exception as e:
        logger.error(f"Error getting mascots: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter mascotes")

@router.get("/active")
async def get_active_mascot():
    """Obter mascote ativo com mensagem contextual"""
    try:
        # Simular dados contextuais do João
        context = MascotContextData(
            totalBalance=15750.0,
            weeklyRevenue=38500.0,
            openOpportunities=8,
            portfolioChange=5.2,
            alertsCount=2,
            tasksCount=5
        )

        # Lógica para determinar qual mascote e mensagem mostrar
        active_mascot = determine_active_mascot(context)
        
        return active_mascot

    except Exception as e:
        logger.error(f"Error getting active mascot: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter mascote ativo")

def determine_active_mascot(context: MascotContextData):
    """Determinar qual mascote deve estar ativo baseado no contexto"""
    
    # Boris - Conservador (aparece quando há riscos ou alertas)
    if context.alertsCount > 0 or context.portfolioChange < 0:
        return {
            "id": "mascot-boris",
            "name": "Boris",
            "personality": "Conservador e analítico. Especialista em gestão de risco.",
            "avatar": "https://images.unsplash.com/photo-1517849845537-4d257902454a?w=200",
            "isActive": True,
            "currentMessage": {
                "id": "msg-boris-001",
                "message": "João, o Bitcoin subiu 5% hoje! Considera realizar alguns lucros? Lembra-te da regra: nunca deixes que a ganância supere a prudência. 🐻",
                "context": "crypto_alert",
                "priority": "MEDIUM",
                "createdAt": datetime.now().isoformat()
            }
        }
    
    # Laya - Otimista (aparece quando há bons resultados)
    elif context.weeklyRevenue > 30000 or context.portfolioChange > 5:
        return {
            "id": "mascot-laya", 
            "name": "Laya",
            "personality": "Otimista e inovadora. Focada em oportunidades de crescimento.",
            "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200",
            "isActive": True,
            "currentMessage": {
                "id": "msg-laya-001",
                "message": "Excelente semana, João! €38.500 em receitas - 3 leads fechadas! O mercado está quente, vamos aproveitar esta onda! 🚀",
                "context": "excellent_week",
                "priority": "LOW",
                "createdAt": datetime.now().isoformat()
            }
        }
    
    # Irina - Estratégica (aparece para revisões e planeamento)
    elif context.tasksCount > 3 or context.openOpportunities > 5:
        return {
            "id": "mascot-irina",
            "name": "Irina", 
            "personality": "Equilibrada e estratégica. Especialista em diversificação.",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200",
            "isActive": True,
            "currentMessage": {
                "id": "msg-irina-001",
                "message": "João, tens 8 oportunidades abertas e 5 tarefas pendentes. Que tal priorizarmos? Sugiro focar na oportunidade do Porto - ROI de 8%! 📊",
                "context": "portfolio_strategy",
                "priority": "MEDIUM",
                "createdAt": datetime.now().isoformat()
            }
        }
    
    # Default - Laya com mensagem de bom dia
    else:
        return {
            "id": "mascot-laya",
            "name": "Laya",
            "personality": "Otimista e inovadora. Focada em oportunidades de crescimento.", 
            "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200",
            "isActive": True,
            "currentMessage": {
                "id": "msg-laya-default",
                "message": "Bom dia, João! Portfolio a €15.750 e estável. Pronto para mais um dia de oportunidades? 💪",
                "context": "daily_greeting",
                "priority": "LOW",
                "createdAt": datetime.now().isoformat()
            }
        }

@router.get("/messages/{mascot_id}")
async def get_mascot_messages(mascot_id: str):
    """Obter mensagens históricas de um mascote"""
    try:
        # Simular mensagens históricas baseadas no mascote
        messages_db = {
            "mascot-boris": [
                {
                    "id": "msg-boris-001",
                    "message": "Recomendo diversificar mais o portfólio. 60% em crypto é arriscado.",
                    "context": "portfolio_review",
                    "priority": "HIGH",
                    "createdAt": "2025-07-06T09:00:00Z"
                },
                {
                    "id": "msg-boris-002", 
                    "message": "Bitcoin muito volátil hoje. Considera stop-loss em 10%.",
                    "context": "risk_management",
                    "priority": "MEDIUM",
                    "createdAt": "2025-07-05T14:30:00Z"
                }
            ],
            "mascot-laya": [
                {
                    "id": "msg-laya-001",
                    "message": "Excelente semana! 3 leads fechadas. O mercado está quente! 🚀",
                    "context": "leads_success", 
                    "priority": "LOW",
                    "createdAt": "2025-07-07T10:00:00Z"
                },
                {
                    "id": "msg-laya-002",
                    "message": "Nova oportunidade DeFi com 12% APY. Vale a pena investigar!",
                    "context": "defi_opportunity",
                    "priority": "MEDIUM", 
                    "createdAt": "2025-07-04T16:45:00Z"
                }
            ],
            "mascot-irina": [
                {
                    "id": "msg-irina-001",
                    "message": "É hora de revisar o portfólio trimestral. Agenda para esta semana?",
                    "context": "quarterly_review",
                    "priority": "MEDIUM",
                    "createdAt": "2025-07-07T08:00:00Z"
                },
                {
                    "id": "msg-irina-002",
                    "message": "Oportunidade imobiliário Porto tem deadline próximo. Priorizar?",
                    "context": "deadline_alert", 
                    "priority": "HIGH",
                    "createdAt": "2025-07-03T11:20:00Z"
                }
            ]
        }

        messages = messages_db.get(mascot_id, [])
        return {"messages": messages}

    except Exception as e:
        logger.error(f"Error getting mascot messages: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter mensagens do mascote")

@router.post("/interact/{mascot_id}")
async def interact_with_mascot(mascot_id: str, message: str):
    """Interagir com um mascote específico"""
    try:
        # Simular resposta baseada no mascote e contexto
        responses = {
            "mascot-boris": [
                "Concordo contigo, João. Prudência é sempre a melhor estratégia.",
                "Vamos analisar os riscos antes de decidir.",
                "Dados históricos mostram que esta pode ser uma boa decisão."
            ],
            "mascot-laya": [
                "Excelente ideia, João! Vamos em frente!",
                "Adoro a tua energia! Esta oportunidade tem potencial.",
                "Sim! O timing está perfeito para este movimento."
            ],
            "mascot-irina": [
                "Interessante perspetiva. Vamos avaliar pros e contras.",
                "Sugiro analisarmos isto em detalhe antes de decidir.",
                "Esta decisão encaixa na nossa estratégia de longo prazo?"
            ]
        }

        mascot_responses = responses.get(mascot_id, ["Obrigado pelo feedback, João!"])
        response = random.choice(mascot_responses)

        return {
            "mascotId": mascot_id,
            "userMessage": message,
            "mascotResponse": response,
            "timestamp": datetime.now().isoformat(),
            "context": "user_interaction"
        }

    except Exception as e:
        logger.error(f"Error interacting with mascot: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao interagir com mascote")

@router.get("/wisdom")
async def get_daily_wisdom():
    """Obter sabedoria financeira diária dos mascotes"""
    try:
        wisdom_pool = [
            {
                "mascot": "Boris",
                "quote": "O investidor inteligente é aquele que nunca perde dinheiro... o genial é aquele que nunca deixa de ganhar.",
                "category": "risk_management"
            },
            {
                "mascot": "Laya", 
                "quote": "As melhores oportunidades surgem quando outros têm medo. Seja corajoso, mas calculista!",
                "category": "opportunities"
            },
            {
                "mascot": "Irina",
                "quote": "Diversificação é a única refeição grátis no mundo dos investimentos.",
                "category": "strategy"
            },
            {
                "mascot": "Boris",
                "quote": "Time in the market beats timing the market - mas só se souberes gerir o risco.",
                "category": "long_term"
            },
            {
                "mascot": "Laya",
                "quote": "Cada 'não' que recebes está mais próximo do próximo 'sim'. Persiste!",
                "category": "mindset"
            }
        ]

        daily_wisdom = random.choice(wisdom_pool)
        
        return {
            "wisdom": daily_wisdom,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "message": f"Sabedoria do dia por {daily_wisdom['mascot']}"
        }

    except Exception as e:
        logger.error(f"Error getting daily wisdom: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter sabedoria diária")

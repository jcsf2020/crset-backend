
from fastapi import APIRouter, HTTPException, Depends
from models import DashboardData, DashboardCard
from database import get_db
import logging
from datetime import datetime, timedelta
import asyncio
import httpx

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/", response_model=DashboardData)
async def get_dashboard_data():
    """Obter dados do dashboard principal"""
    try:
        # Simular query à base de dados para dados reais
        # Em produção, estas seriam queries reais ao Prisma/PostgreSQL
        
        # Cards principais
        cards = [
            DashboardCard(
                title="Saldo Atual",
                value="€15.750",
                change="+5.2%",
                changeType="positive",
                icon="wallet",
                description="Portfolio total"
            ),
            DashboardCard(
                title="Leads Abertas",
                value="8",
                change="3 fechadas esta semana",
                changeType="positive",
                icon="target",
                description="Oportunidades ativas"
            ),
            DashboardCard(
                title="Alertas",
                value="2",
                change="Bitcoin +5% hoje",
                changeType="neutral",
                icon="bell",
                description="Requerem atenção"
            ),
            DashboardCard(
                title="Tarefas",
                value="5",
                change="2 urgentes",
                changeType="warning",
                icon="list-todo",
                description="Pendentes"
            )
        ]

        # Transações recentes (simuladas)
        recent_transactions = [
            {
                "id": "tx-001",
                "type": "INCOME",
                "amount": 18000.0,
                "description": "Consultoria Bancária Digital - Millennium BCP",
                "date": "2025-07-07",
                "category": "Consultoria"
            },
            {
                "id": "tx-002", 
                "type": "INCOME",
                "amount": 12000.0,
                "description": "Assessoria Investimento Particular - Cliente VIP",
                "date": "2025-07-06",
                "category": "Assessoria"
            },
            {
                "id": "tx-003",
                "type": "INCOME", 
                "amount": 8500.0,
                "description": "Workshop Empresas Tech - Tech Hub Lisboa",
                "date": "2025-07-05",
                "category": "Formação"
            },
            {
                "id": "tx-004",
                "type": "INVESTMENT",
                "amount": -2000.0,
                "description": "Compra adicional BTC - DCA strategy",
                "date": "2025-07-01",
                "category": "Crypto"
            }
        ]

        # Alertas ativos
        alerts = [
            {
                "id": "alert-001",
                "title": "Bitcoin +5% hoje",
                "message": "O Bitcoin subiu 5% nas últimas 24h. Considera realizar lucros?",
                "type": "SUCCESS",
                "priority": "MEDIUM",
                "isRead": False
            },
            {
                "id": "alert-002",
                "title": "Oportunidade Imobiliário Porto", 
                "message": "Apartamento T2 no Porto com ROI 8%/ano. Mercado aquecido.",
                "type": "INFO",
                "priority": "HIGH",
                "isRead": False
            }
        ]

        # Tarefas pendentes
        tasks = [
            {
                "id": "task-001",
                "title": "Revisar portfólio trimestral",
                "description": "Análise de performance Q3 e rebalanceamento",
                "priority": "HIGH",
                "dueDate": "2025-07-15",
                "isCompleted": False
            },
            {
                "id": "task-002",
                "title": "Contactar lead TechCorp",
                "description": "Follow-up da proposta de parceria",
                "priority": "HIGH", 
                "dueDate": "2025-07-10",
                "isCompleted": False
            },
            {
                "id": "task-003",
                "title": "Atualizar declaração fiscal",
                "description": "Preparar documentos para crypto gains",
                "priority": "HIGH",
                "dueDate": "2025-07-31", 
                "isCompleted": False
            }
        ]

        return DashboardData(
            cards=cards,
            recentTransactions=recent_transactions,
            alerts=alerts,
            tasks=tasks,
            totalBalance=15750.0,
            weeklyRevenue=38500.0,  # 3 leads fechadas
            portfolioGrowth=5.2
        )

    except Exception as e:
        logger.error(f"Error getting dashboard data: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter dados do dashboard")

@router.get("/stats")
async def get_dashboard_stats():
    """Obter estatísticas resumidas do dashboard"""
    return {
        "totalBalance": 15750.0,
        "weeklyRevenue": 38500.0,
        "monthlyGrowth": 12.8,
        "yearlyGrowth": 45.2,
        "assetsCount": 4,
        "opportunitiesCount": 8,
        "tasksCount": 5,
        "alertsCount": 2
    }

@router.get("/recent-activity")
async def get_recent_activity():
    """Obter atividade recente"""
    return {
        "activities": [
            {
                "id": "act-001",
                "type": "lead_closed",
                "title": "Lead fechada - Millennium BCP",
                "description": "Consultoria Bancária Digital - €18.000",
                "timestamp": "2025-07-07T10:30:00Z",
                "icon": "check-circle"
            },
            {
                "id": "act-002", 
                "type": "crypto_alert",
                "title": "Bitcoin subiu 5%",
                "description": "Oportunidade de realizar lucros",
                "timestamp": "2025-07-07T08:15:00Z",
                "icon": "trending-up"
            },
            {
                "id": "act-003",
                "type": "investment",
                "title": "Compra BTC",
                "description": "DCA strategy - €2.000 investidos",
                "timestamp": "2025-07-01T14:20:00Z",
                "icon": "bitcoin"
            }
        ]
    }

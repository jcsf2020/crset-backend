
from fastapi import APIRouter, HTTPException
from models import SimulatorInput, SimulatorResult
import logging
import math

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/calculate", response_model=SimulatorResult)
async def calculate_returns(input_data: SimulatorInput):
    """Calcular projeções de rendimento com juros compostos"""
    try:
        initial = input_data.initialAmount
        monthly_contribution = input_data.monthlyContribution
        annual_rate = input_data.annualReturn / 100  # Converter percentagem
        years = input_data.timeHorizon
        compounds_per_year = input_data.compoundFrequency

        # Calcular projeções mensais e anuais
        monthly_projections = []
        yearly_projections = []
        
        current_amount = initial
        total_contributions = initial
        monthly_rate = annual_rate / compounds_per_year

        for month in range(1, years * 12 + 1):
            # Adicionar contribuição mensal
            if month > 1:  # Não adicionar no primeiro mês (já temos o valor inicial)
                current_amount += monthly_contribution
                total_contributions += monthly_contribution
            
            # Aplicar juros compostos
            current_amount = current_amount * (1 + monthly_rate)
            
            monthly_projections.append({
                "month": month,
                "balance": round(current_amount, 2),
                "contributions": round(total_contributions, 2),
                "gains": round(current_amount - total_contributions, 2)
            })
            
            # Guardar projeção anual
            if month % 12 == 0:
                year = month // 12
                yearly_projections.append({
                    "year": year,
                    "balance": round(current_amount, 2),
                    "contributions": round(total_contributions, 2),
                    "gains": round(current_amount - total_contributions, 2),
                    "yearlyReturn": round(((current_amount / total_contributions - 1) * 100), 2)
                })

        final_amount = current_amount
        total_gains = final_amount - total_contributions

        result = SimulatorResult(
            initialAmount=initial,
            monthlyContribution=monthly_contribution,
            annualReturn=input_data.annualReturn,
            timeHorizon=years,
            finalAmount=round(final_amount, 2),
            totalContributions=round(total_contributions, 2),
            totalGains=round(total_gains, 2),
            monthlyProjections=monthly_projections[-12:],  # Últimos 12 meses
            yearlyProjections=yearly_projections
        )

        logger.info(f"Simulation calculated: €{initial} -> €{final_amount:.2f} over {years} years")
        return result

    except Exception as e:
        logger.error(f"Error calculating simulation: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao calcular simulação")

@router.get("/presets")
async def get_simulation_presets():
    """Obter presets de simulação comuns"""
    return {
        "conservative": {
            "name": "Conservador",
            "annualReturn": 4.0,
            "description": "Investimentos de baixo risco",
            "examples": ["Certificados de Aforro", "Depósitos a prazo"]
        },
        "moderate": {
            "name": "Moderado",
            "annualReturn": 7.0,
            "description": "Mix equilibrado de investimentos",
            "examples": ["ETFs diversificados", "Fundos mistos"]
        },
        "aggressive": {
            "name": "Agressivo",
            "annualReturn": 12.0,
            "description": "Investimentos de alto risco/retorno",
            "examples": ["Ações individuais", "Crypto", "Startups"]
        },
        "crypto": {
            "name": "Crypto DeFi",
            "annualReturn": 15.0,
            "description": "Estratégias DeFi e staking",
            "examples": ["Staking ETH", "Liquidity pools", "DeFi protocols"]
        }
    }

@router.post("/scenarios")
async def compare_scenarios(scenarios: list[SimulatorInput]):
    """Comparar múltiplos cenários de investimento"""
    try:
        results = []
        
        for i, scenario in enumerate(scenarios):
            # Reutilizar lógica do calculate_returns
            initial = scenario.initialAmount
            monthly_contribution = scenario.monthlyContribution
            annual_rate = scenario.annualReturn / 100
            years = scenario.timeHorizon
            
            # Cálculo simplificado para comparação
            total_contributions = initial + (monthly_contribution * 12 * years)
            
            # Fórmula de juros compostos com contribuições mensais
            if monthly_contribution > 0:
                monthly_rate = annual_rate / 12
                months = years * 12
                future_value_initial = initial * ((1 + monthly_rate) ** months)
                future_value_annuity = monthly_contribution * (((1 + monthly_rate) ** months - 1) / monthly_rate)
                final_amount = future_value_initial + future_value_annuity
            else:
                final_amount = initial * ((1 + annual_rate) ** years)
            
            results.append({
                "scenario": f"Cenário {i + 1}",
                "initialAmount": initial,
                "monthlyContribution": monthly_contribution,
                "annualReturn": scenario.annualReturn,
                "timeHorizon": years,
                "finalAmount": round(final_amount, 2),
                "totalContributions": round(total_contributions, 2),
                "totalGains": round(final_amount - total_contributions, 2),
                "roi": round(((final_amount / total_contributions - 1) * 100), 2)
            })
        
        # Ordenar por ROI descendente
        results.sort(key=lambda x: x["roi"], reverse=True)
        
        return {
            "scenarios": results,
            "bestScenario": results[0] if results else None,
            "comparison": {
                "maxReturn": max(r["finalAmount"] for r in results) if results else 0,
                "minReturn": min(r["finalAmount"] for r in results) if results else 0,
                "avgReturn": sum(r["finalAmount"] for r in results) / len(results) if results else 0
            }
        }

    except Exception as e:
        logger.error(f"Error comparing scenarios: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao comparar cenários")

@router.get("/portfolio-projection")
async def get_portfolio_projection():
    """Projeção baseada no portfolio atual do João"""
    try:
        # Baseado nos ativos atuais do João (€15.750)
        current_portfolio = 15750.0
        
        # Diferentes cenários baseados na composição atual
        scenarios = [
            {
                "name": "Manter Atual",
                "description": "Manter composição atual (74% crypto, 16% cash, 10% business)",
                "expectedReturn": 8.5,
                "risk": "Alto"
            },
            {
                "name": "Diversificado",
                "description": "Rebalancear: 40% crypto, 30% ETFs, 20% cash, 10% business",
                "expectedReturn": 7.2,
                "risk": "Médio"
            },
            {
                "name": "Conservador",
                "description": "Reduzir crypto: 20% crypto, 40% ETFs, 30% cash, 10% business",
                "expectedReturn": 5.8,
                "risk": "Baixo"
            }
        ]

        projections = []
        for scenario in scenarios:
            years = [1, 3, 5, 10]
            scenario_projections = []
            
            for year in years:
                rate = scenario["expectedReturn"] / 100
                final_amount = current_portfolio * ((1 + rate) ** year)
                gain = final_amount - current_portfolio
                
                scenario_projections.append({
                    "year": year,
                    "amount": round(final_amount, 2),
                    "gain": round(gain, 2),
                    "gainPercentage": round((gain / current_portfolio) * 100, 1)
                })
            
            projections.append({
                "scenario": scenario,
                "projections": scenario_projections
            })

        return {
            "currentPortfolio": current_portfolio,
            "scenarios": projections,
            "recommendations": [
                "Considerar diversificação para reduzir risco de crypto",
                "Manter reserva de emergência em cash",
                "Explorar ETFs para exposição a ações globais",
                "Avaliar oportunidades de rendimento passivo"
            ]
        }

    except Exception as e:
        logger.error(f"Error getting portfolio projection: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter projeção do portfolio")


from fastapi import APIRouter, HTTPException, Depends
from models import AssetCreate, AssetUpdate, AssetResponse, SuccessResponse
from database import get_db
from typing import List, Optional
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/", response_model=List[AssetResponse])
async def get_assets(
    type: Optional[str] = None,
    active_only: bool = True
):
    """Obter lista de ativos"""
    try:
        # Simular dados dos ativos (em produção seriam queries reais)
        assets = [
            {
                "id": "asset-001",
                "name": "Bitcoin Holdings", 
                "type": "CRYPTO",
                "value": 8500.0,
                "purchaseDate": "2024-01-15T00:00:00Z",
                "description": "0.2 BTC adquirida em várias compras",
                "location": None,
                "currency": "EUR",
                "imageUrl": "https://thumbs.dreamstime.com/z/tangible-representation-bitcoin-emerges-as-physical-coin-blending-digital-physical-symbolic-fusion-300851184.jpg",
                "isActive": True,
                "createdAt": "2024-01-15T00:00:00Z",
                "updatedAt": "2025-07-07T00:00:00Z"
            },
            {
                "id": "asset-002",
                "name": "Ethereum Holdings",
                "type": "CRYPTO", 
                "value": 3200.0,
                "purchaseDate": "2024-02-10T00:00:00Z",
                "description": "1.5 ETH para diversificação crypto",
                "location": None,
                "currency": "EUR",
                "imageUrl": "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=400",
                "isActive": True,
                "createdAt": "2024-02-10T00:00:00Z",
                "updatedAt": "2025-07-07T00:00:00Z"
            },
            {
                "id": "asset-003",
                "name": "Conta Poupança BCP",
                "type": "CASH",
                "value": 2500.0,
                "purchaseDate": None,
                "description": "Reserva de emergência",
                "location": None,
                "currency": "EUR", 
                "imageUrl": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400",
                "isActive": True,
                "createdAt": "2023-06-01T00:00:00Z",
                "updatedAt": "2025-07-07T00:00:00Z"
            },
            {
                "id": "asset-004",
                "name": "CRSET Solutions",
                "type": "BUSINESS",
                "value": 1550.0,
                "purchaseDate": "2023-06-01T00:00:00Z",
                "description": "Participação na empresa de consultoria",
                "location": "Portugal",
                "currency": "EUR",
                "imageUrl": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=400",
                "isActive": True,
                "createdAt": "2023-06-01T00:00:00Z", 
                "updatedAt": "2025-07-07T00:00:00Z"
            }
        ]

        # Filtrar por tipo se especificado
        if type:
            assets = [asset for asset in assets if asset["type"] == type.upper()]

        # Filtrar apenas ativos ativos se especificado
        if active_only:
            assets = [asset for asset in assets if asset["isActive"]]

        return assets

    except Exception as e:
        logger.error(f"Error getting assets: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao obter ativos")

@router.get("/{asset_id}", response_model=AssetResponse)
async def get_asset(asset_id: str):
    """Obter ativo específico"""
    # Simular obtenção de ativo específico
    # Em produção seria uma query real à base de dados
    mock_asset = {
        "id": asset_id,
        "name": "Bitcoin Holdings",
        "type": "CRYPTO",
        "value": 8500.0,
        "purchaseDate": "2024-01-15T00:00:00Z",
        "description": "0.2 BTC adquirida em várias compras",
        "location": None,
        "currency": "EUR",
        "imageUrl": "https://thumbs.dreamstime.com/b/bitcoin-cryptocurrency-background-market-chart-representing-digital-currencies-financial-trading-shiny-placed-against-327038704.jpg",
        "isActive": True,
        "createdAt": "2024-01-15T00:00:00Z",
        "updatedAt": "2025-07-07T00:00:00Z"
    }
    return mock_asset

@router.post("/", response_model=AssetResponse)
async def create_asset(asset: AssetCreate):
    """Criar novo ativo"""
    try:
        # Em produção, salvaria na base de dados via Prisma
        new_asset = {
            "id": f"asset-new-{asset.name.lower().replace(' ', '-')}",
            "name": asset.name,
            "type": asset.type,
            "value": asset.value,
            "purchaseDate": asset.purchaseDate.isoformat() if asset.purchaseDate else None,
            "description": asset.description,
            "location": asset.location,
            "currency": asset.currency,
            "imageUrl": asset.imageUrl,
            "isActive": True,
            "createdAt": "2025-07-07T00:00:00Z",
            "updatedAt": "2025-07-07T00:00:00Z"
        }

        logger.info(f"Asset created: {new_asset['name']} - €{new_asset['value']}")
        return new_asset

    except Exception as e:
        logger.error(f"Error creating asset: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao criar ativo")

@router.put("/{asset_id}", response_model=AssetResponse)
async def update_asset(asset_id: str, asset: AssetUpdate):
    """Atualizar ativo existente"""
    try:
        # Em produção seria uma query real de atualização
        updated_asset = {
            "id": asset_id,
            "name": asset.name or "Bitcoin Holdings",
            "type": asset.type or "CRYPTO",
            "value": asset.value or 8500.0,
            "purchaseDate": asset.purchaseDate.isoformat() if asset.purchaseDate else "2024-01-15T00:00:00Z",
            "description": asset.description or "0.2 BTC adquirida em várias compras",
            "location": asset.location,
            "currency": asset.currency or "EUR",
            "imageUrl": asset.imageUrl or "https://c8.alamy.com/comp/KPJYC4/conceptual-artwork-representing-the-bitcoin-cryptocurrency-bitcoin-KPJYC4.jpg",
            "isActive": asset.isActive if asset.isActive is not None else True,
            "createdAt": "2024-01-15T00:00:00Z",
            "updatedAt": "2025-07-07T00:00:00Z"
        }

        logger.info(f"Asset updated: {asset_id}")
        return updated_asset

    except Exception as e:
        logger.error(f"Error updating asset: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar ativo")

@router.delete("/{asset_id}")
async def delete_asset(asset_id: str):
    """Eliminar ativo"""
    try:
        # Em produção seria uma query de delete ou soft delete
        logger.info(f"Asset deleted: {asset_id}")
        return SuccessResponse(message=f"Ativo {asset_id} eliminado com sucesso")

    except Exception as e:
        logger.error(f"Error deleting asset: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao eliminar ativo")

@router.get("/summary/totals")
async def get_assets_summary():
    """Obter resumo dos ativos"""
    return {
        "totalValue": 15750.0,
        "totalAssets": 4,
        "byType": {
            "CRYPTO": {"value": 11700.0, "count": 2},
            "CASH": {"value": 2500.0, "count": 1},
            "BUSINESS": {"value": 1550.0, "count": 1}
        },
        "byCurrency": {
            "EUR": 15750.0
        },
        "monthlyGrowth": 5.2,
        "yearlyGrowth": 23.8
    }

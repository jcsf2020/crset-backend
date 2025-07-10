
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

# Enums
class AssetType(str, Enum):
    CRYPTO = "CRYPTO"
    REAL_ESTATE = "REAL_ESTATE"
    STOCKS = "STOCKS"
    BONDS = "BONDS"
    BUSINESS = "BUSINESS"
    CASH = "CASH"
    OTHER = "OTHER"

class OpportunityType(str, Enum):
    INVESTMENT = "INVESTMENT"
    REAL_ESTATE = "REAL_ESTATE"
    CRYPTO = "CRYPTO"
    BUSINESS = "BUSINESS"
    PARTNERSHIP = "PARTNERSHIP"
    PROJECT = "PROJECT"
    OTHER = "OTHER"

class OpportunityStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED_WON = "CLOSED_WON"
    CLOSED_LOST = "CLOSED_LOST"
    ON_HOLD = "ON_HOLD"

class TransactionType(str, Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    INVESTMENT = "INVESTMENT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER = "TRANSFER"

class AlertType(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"

# Dashboard Models
class DashboardCard(BaseModel):
    title: str
    value: str
    change: Optional[str] = None
    changeType: Optional[str] = None  # "positive", "negative", "neutral"
    icon: str
    description: Optional[str] = None

class DashboardData(BaseModel):
    cards: List[DashboardCard]
    recentTransactions: List[dict]
    alerts: List[dict]
    tasks: List[dict]
    totalBalance: float
    weeklyRevenue: float
    portfolioGrowth: float

# Asset Models
class AssetCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    type: AssetType
    value: float = Field(..., gt=0)
    purchaseDate: Optional[datetime] = None
    description: Optional[str] = None
    location: Optional[str] = None
    currency: str = Field(default="EUR", max_length=3)
    imageUrl: Optional[str] = None

class AssetUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[AssetType] = None
    value: Optional[float] = None
    purchaseDate: Optional[datetime] = None
    description: Optional[str] = None
    location: Optional[str] = None
    currency: Optional[str] = None
    imageUrl: Optional[str] = None
    isActive: Optional[bool] = None

class AssetResponse(BaseModel):
    id: str
    name: str
    type: AssetType
    value: float
    purchaseDate: Optional[datetime]
    description: Optional[str]
    location: Optional[str]
    currency: str
    imageUrl: Optional[str]
    isActive: bool
    createdAt: datetime
    updatedAt: datetime

# Opportunity Models
class OpportunityCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    type: OpportunityType
    status: OpportunityStatus = OpportunityStatus.OPEN
    value: Optional[float] = None
    priority: Priority = Priority.MEDIUM
    deadline: Optional[datetime] = None
    contact: Optional[str] = None
    notes: Optional[str] = None
    tags: List[str] = []

class OpportunityUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[OpportunityType] = None
    status: Optional[OpportunityStatus] = None
    value: Optional[float] = None
    priority: Optional[Priority] = None
    deadline: Optional[datetime] = None
    contact: Optional[str] = None
    notes: Optional[str] = None
    tags: Optional[List[str]] = None

class OpportunityResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    type: OpportunityType
    status: OpportunityStatus
    value: Optional[float]
    priority: Priority
    deadline: Optional[datetime]
    contact: Optional[str]
    notes: Optional[str]
    tags: List[str]
    createdAt: datetime
    updatedAt: datetime

# Simulator Models
class SimulatorInput(BaseModel):
    initialAmount: float = Field(..., gt=0)
    monthlyContribution: float = Field(default=0, ge=0)
    annualReturn: float = Field(..., gt=0, le=100)  # Percentage
    timeHorizon: int = Field(..., gt=0, le=50)  # Years
    compoundFrequency: int = Field(default=12, gt=0)  # Times per year

class SimulatorResult(BaseModel):
    initialAmount: float
    monthlyContribution: float
    annualReturn: float
    timeHorizon: int
    finalAmount: float
    totalContributions: float
    totalGains: float
    monthlyProjections: List[dict]
    yearlyProjections: List[dict]

# Transaction Models
class TransactionCreate(BaseModel):
    type: TransactionType
    amount: float
    description: Optional[str] = None
    date: Optional[datetime] = None
    category: Optional[str] = None
    assetId: Optional[str] = None

class TransactionResponse(BaseModel):
    id: str
    type: TransactionType
    amount: float
    currency: str
    description: Optional[str]
    date: datetime
    category: Optional[str]
    createdAt: datetime

# Mascot Models
class MascotMessage(BaseModel):
    id: str
    message: str
    context: Optional[str]
    priority: Priority
    createdAt: datetime

class MascotResponse(BaseModel):
    id: str
    name: str
    personality: str
    avatar: Optional[str]
    isActive: bool
    currentMessage: Optional[MascotMessage] = None

class MascotContextData(BaseModel):
    totalBalance: float
    weeklyRevenue: float
    openOpportunities: int
    portfolioChange: float
    alertsCount: int
    tasksCount: int

# Export Models
class ExportType(str, Enum):
    PDF = "pdf"
    EXCEL = "excel"

class ExportRequest(BaseModel):
    type: ExportType
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    includeAssets: bool = True
    includeOpportunities: bool = True
    includeTransactions: bool = True

# Response Models
class SuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: Optional[dict] = None

class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    message: str
    timestamp: datetime = Field(default_factory=datetime.now)

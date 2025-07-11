from fastapi import APIRouter
import stripe
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@router.post("/create-checkout-session")
def create_checkout_session():
    return {"status": "checkout created"}

"""Payment endpoints."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/payments", tags=["payments"])


class PaymentRequest(BaseModel):
    user_id: str
    amount: float


@router.post("/charge")
def charge(req: PaymentRequest):
    """Pretend to process a payment."""
    return {"status": "charged", "user_id": req.user_id, "amount": req.amount}


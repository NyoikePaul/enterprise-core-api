import httpx
import base64
from datetime import datetime
from src.core.config import settings


class MpesaService:
    """
    Expert-level service for handling Safaricom Daraja API integrations.
    Supports async STK Push and OAuth2 token management.
    """

    def __init__(self):
        self.base_url = settings.MPESA_BASE_URL
        self.consumer_key = settings.MPESA_CONSUMER_KEY
        self.consumer_secret = settings.MPESA_CONSUMER_SECRET

    async def get_access_token(self) -> str:
        """Fetch and return a valid OAuth2 token."""
        url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url, auth=(self.consumer_key, self.consumer_secret)
            )
            response.raise_for_status()
            return response.json()["access_token"]

    async def stk_push(self, phone: str, amount: int, description: str):
        """Initiate an STK Push (Lipa na M-Pesa Online)."""
        token = await self.get_access_token()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        password = base64.b64encode(
            f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode()
        ).decode()

        payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": settings.MPESA_SHORTCODE,
            "PhoneNumber": phone,
            "CallBackURL": settings.MPESA_CALLBACK_URL,
            "AccountReference": "EnterpriseCoreAPI",
            "TransactionDesc": description,
        }

        headers = {"Authorization": f"Bearer {token}"}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/mpesa/stkpush/v1/processrequest",
                json=payload,
                headers=headers,
            )
            return response.json()

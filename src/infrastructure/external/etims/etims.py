import httpx
from src.core.config import settings
from src.schemas.etims import ETIMSInvoice


class ETIMSService:
    """Handles secure transmission of invoices to KRA eTIMS portal."""

    def __init__(self):
        self.url = f"{settings.ETIMS_BASE_URL}/invoice/save"
        self.device_serial = settings.ETIMS_DEVICE_SERIAL

    async def transmit_invoice(self, invoice: ETIMSInvoice):
        async with httpx.AsyncClient() as client:
            # Expert Tip: Add custom headers for device authentication
            headers = {"X-Device-Serial": self.device_serial}
            response = await client.post(
                self.url, json=invoice.model_dump(), headers=headers
            )
            response.raise_for_status()
            return response.json()

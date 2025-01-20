from .config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME
from .models import fetch_payments, create_payment, update_payment, delete_payment
from .schemas import PaymentSchema, UpdatePaymentSchema

import logging

# Set up logging for the app
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Metadata about the app
__version__ = "1.0.0"
__author__ = "Mohammad Amin Najaflou"

logger.info("App package initialized.")

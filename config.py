import os
from dotenv import load_dotenv

load_dotenv()

AUTH_ON = os.getenv("AUTH_ON", "false").lower() == "true"

VALID_TOKENS = [os.getenv("DEV_API_TOKEN"), os.getenv("PROD_API_TOKEN")]

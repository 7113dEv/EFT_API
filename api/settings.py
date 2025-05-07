import os

from config_loader import load_config

current_env = os.getenv("ENVIRONMENT", "dev")
config = load_config().get(current_env, {})

# Run Constants
DEBUG = config.get("DEBUG", False)

# DB Constants
DATABASE_URI = config.get("DATABASE_URI", "mysql://root:password123@localhost:3307/eft-db")

# API Constants
TARKOV_DEV_API_URL = config.get("TARKOV_DEV_API_URL", "")

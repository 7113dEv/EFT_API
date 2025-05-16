import os

from config_loader import load_config

current_env = os.getenv("ENVIRONMENT", "dev")
config = load_config().get(current_env, {})

# Run Constants
DEBUG = config.get("DEBUG", False)

# DB
DATABASE_URI = config.get("DATABASE_URI", "")

# API
TARKOV_DEV_API_URL = config.get("TARKOV_DEV_API_URL", "")

# Redis
REDIS_URL = config.get("REDIS_URL", os.getenv("REDIS_URL", "redis://:password123@localhost:6379/0"))

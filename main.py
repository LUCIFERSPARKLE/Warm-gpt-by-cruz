import os
import sys
import logging
from dotenv import load_dotenv

# === Load .env FIRST before anything else ===
load_dotenv()

# === Validate required env vars ===
required_vars = ["TELEGRAM_TOKEN", "OPENROUTER_KEY"]
missing = [v for v in required_vars if not os.getenv(v)]
if missing:
    print(f"❌ Missing environment variables: {', '.join(missing)}")
    print("   Create a .env file or set them in your hosting platform.")
    sys.exit(1)

# === Set Owner ID if not already set ===
if not os.getenv("OWNER_ID"):
    os.environ["OWNER_ID"] = "8705127026"

from keep_alive import keep_alive
import telegram_bot

if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    
    owner_id = os.getenv("OWNER_ID", "8705127026")
    logger = logging.getLogger(__name__)
    logger.info(f"👑 Bot Owner ID: {owner_id}")

    keep_alive()
    telegram_bot.run_bot()

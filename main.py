import os
import sys
import logging
from dotenv import load_dotenv

# === Load .env FIRST before anything else ===
load_dotenv()

# === Validate required env vars ===
required_vars = ["8267095618:AAFKUedUQkPvz99oPY64f1H7DmWZUNMV9_E", "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"]
missing = [v for v in required_vars if not os.getenv(v)]
if missing:
    print(f"❌ Missing environment variables: {', '.join(missing)}")
    print("   Create a .env file or set them in your hosting platform.")
    sys.exit(1)

from keep_alive import keep_alive
import telegram_bot

if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)

    keep_alive()
    telegram_bot.run_bot()

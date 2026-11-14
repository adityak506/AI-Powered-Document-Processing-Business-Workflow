import os
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base Directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

STRUCTURED_DIR = OUTPUT_DIR / "structured_data"
EMAILS_DIR = OUTPUT_DIR / "customer_emails"
SUMMARIES_DIR = OUTPUT_DIR / "case_summaries"
FINAL_REPORT_PATH = OUTPUT_DIR / "final_report.csv"

# Ensure output directories exist
for directory in [STRUCTURED_DIR, EMAILS_DIR, SUMMARIES_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# LLM Settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

# Logging Configuration[cite: 1]
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(OUTPUT_DIR / "workflow.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ComplaintProcessor")
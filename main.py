import pandas as pd
from src.config import DATA_DIR, FINAL_REPORT_PATH, OPENAI_API_KEY, logger
from src.ingestion import SUPPORTED_EXTENSIONS
from src.workflow import process_single_document

def run_batch():
    if not OPENAI_API_KEY:
        raise EnvironmentError("OPENAI_API_KEY is missing. Set it in your .env file.")

    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True)
        logger.warning(f"Created empty {DATA_DIR}. Add documents and re-run.")
        return

    files = [
        f for f in sorted(DATA_DIR.iterdir())
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not files:
        logger.warning(f"No supported files found in {DATA_DIR}.")
        return

    logger.info(f"Starting batch processing for {len(files)} document(s)...")
    consolidated_records = []

    for file_path in files:
        try:
            record = process_single_document(file_path)
            consolidated_records.append(record)
        except Exception as e:
            logger.error(f"Skipping {file_path.name} due to error: {e}")
            consolidated_records.append({
                "source_file": file_path.name,
                "overall_case_status": f"ERROR: {str(e)}"
            })

    # Generate Consolidated CSV Report[cite: 1]
    df = pd.DataFrame(consolidated_records)
    df.to_csv(FINAL_REPORT_PATH, index=False, encoding="utf-8")
    logger.info(f"Batch complete. Final report saved to {FINAL_REPORT_PATH}")

if __name__ == "__main__":
    run_batch()
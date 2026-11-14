from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Dict, Any
from src.config import STRUCTURED_DIR, EMAILS_DIR, SUMMARIES_DIR, logger
from src.ingestion import extract_text_from_file
from src.llm_tasks import (
    extract_structured_data,
    generate_customer_email,
    generate_management_summary,
)

def process_single_document(file_path: Path) -> Dict[str, Any]:
    """Runs the complete AI workflow for a single document."""
    stem = file_path.stem
    logger.info(f"Processing document: {file_path.name}")

    # Step 1: Ingest Text
    raw_text = extract_text_from_file(file_path)

    # Step 2: Structured Extraction (Sequential prerequisite)
    extracted_data = extract_structured_data(raw_text)

    # Step 3: Parallel Execution of Customer Email & Management Summary
    with ThreadPoolExecutor(max_workers=2) as executor:
        email_future = executor.submit(generate_customer_email, extracted_data, raw_text)
        summary_future = executor.submit(generate_management_summary, extracted_data, raw_text)

        customer_email = email_future.result()
        case_summary = summary_future.result()

    # Step 4: Persist Individual Artifacts
    json_path = STRUCTURED_DIR / f"{stem}.json"
    email_path = EMAILS_DIR / f"{stem}_email.txt"
    summary_path = SUMMARIES_DIR / f"{stem}_summary.md"

    json_path.write_text(extracted_data.model_dump_json(indent=2), encoding="utf-8")
    email_path.write_text(customer_email, encoding="utf-8")
    summary_path.write_text(case_summary, encoding="utf-8")

    logger.info(f"Completed processing: {file_path.name}")

    # Return flattened record for final_report.csv
    record = {"source_file": file_path.name, **extracted_data.model_dump()}
    return record
import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s"
)

PROJECT_NAME = "customer-complaint-processor"

# Directories to create explicitly (including empty output subdirectories)
DIRECTORIES = [
    f"{PROJECT_NAME}/data",
    f"{PROJECT_NAME}/output/structured_data",
    f"{PROJECT_NAME}/output/customer_emails",
    f"{PROJECT_NAME}/output/case_summaries",
    f"{PROJECT_NAME}/src",
]

# Files to create
FILES = [
    f"{PROJECT_NAME}/data/complaint_001.txt",
    f"{PROJECT_NAME}/data/complaint_002.docx",
    f"{PROJECT_NAME}/output/final_report.csv",
    f"{PROJECT_NAME}/src/__init__.py",
    f"{PROJECT_NAME}/src/config.py",
    f"{PROJECT_NAME}/src/schemas.py",
    f"{PROJECT_NAME}/src/ingestion.py",
    f"{PROJECT_NAME}/src/llm_tasks.py",
    f"{PROJECT_NAME}/src/workflow.py",
    f"{PROJECT_NAME}/main.py",
    f"{PROJECT_NAME}/requirements.txt",
    f"{PROJECT_NAME}/.env.example",
    f"{PROJECT_NAME}/README.md",
]


def create_project_structure() -> None:
    logging.info(f"Scaffolding project structure for '{PROJECT_NAME}'...")

    # Create all directories
    for dir_path in DIRECTORIES:
        path = Path(dir_path)
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {path}")

    # Create empty files if they do not already exist (or are empty)
    for file_path in FILES:
        path = Path(file_path)
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)

        if not path.exists() or path.stat().st_size == 0:
            path.touch()
            logging.info(f"Created file:      {path}")
        else:
            logging.info(f"Skipped (exists):  {path}")

    logging.info("Project scaffolding complete!")


if __name__ == "__main__":
    create_project_structure()
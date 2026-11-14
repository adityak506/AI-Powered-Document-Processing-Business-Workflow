from pathlib import Path
from pypdf import PdfReader
import docx
from src.config import logger

SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx"}

def extract_text_from_file(file_path: Path) -> str:
    """Extracts raw text from .txt, .pdf, or .docx files with error handling."""
    ext = file_path.suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file format: {ext}")

    try:
        if ext == ".txt":
            return file_path.read_text(encoding="utf-8").strip()

        elif ext == ".pdf":
            reader = PdfReader(str(file_path))
            pages = [page.extract_text() or "" for page in reader.pages]
            text = "\n".join(pages).strip()
            if not text:
                raise ValueError("PDF contains no extractable text (may be scanned).")
            return text

        elif ext == ".docx":
            doc = docx.Document(str(file_path))
            paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
            return "\n".join(paragraphs).strip()

    except Exception as e:
        logger.error(f"Failed to read {file_path.name}: {e}")
        raise
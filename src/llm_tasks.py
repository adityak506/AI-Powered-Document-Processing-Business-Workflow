import json
from openai import OpenAI
from src.config import OPENAI_API_KEY, MODEL_NAME
from src.schemas import ComplaintExtraction

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_structured_data(document_text: str) -> ComplaintExtraction:
    """Task 1: Extract structured fields adhering strictly to the Pydantic schema."""
    response = client.beta.chat.completions.parse(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise data extraction assistant. Extract customer complaint details "
                    "strictly from the provided text. Do not invent or assume missing facts."
                ),
            },
            {"role": "user", "content": f"Document Content:\n\n{document_text}"},
        ],
        response_format=ComplaintExtraction,
        temperature=0.0,
    )
    return response.choices[0].message.parsed


def generate_customer_email(extracted: ComplaintExtraction, raw_text: str) -> str:
    """Task 2: Generate a grounded, empathetic customer response email."""
    structured_json = extracted.model_dump_json(indent=2)
    prompt = f"""
    Write a professional customer support response email based ONLY on the verified case details below.
    
    Rules:
    - Address the customer appropriately by name (if 'Unknown', use 'Valued Customer').
    - Summarize their issue clearly.
    - Mention the resolution provided or current case status.
    - Maintain a polite, empathetic, and professional tone.
    - CRITICAL: Do NOT invent refund amounts, timelines, policies, or facts not present in the source.

    Extracted Data:
    {structured_json}

    Original Document Context:
    {raw_text}
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


def generate_management_summary(extracted: ComplaintExtraction, raw_text: str) -> str:
    """Task 3: Generate a concise internal management summary."""
    structured_json = extracted.model_dump_json(indent=2)
    prompt = f"""
    Create a concise internal management case summary using Markdown formatting.
    Include exact sections for:
    - **Case Overview**
    - **Key Issue**
    - **Action Taken**
    - **Current Status**
    - **Recommended Next Action**

    Base this strictly on the facts provided below.

    Extracted Data:
    {structured_json}

    Original Document Context:
    {raw_text}
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()
from typing import Literal, Optional
from pydantic import BaseModel, Field

class ComplaintExtraction(BaseModel):
    customer_name: str = Field(description="Full name of the customer, or 'Unknown' if missing.")
    email: Optional[str] = Field(default=None, description="Customer email address if provided.")
    phone_number: Optional[str] = Field(default=None, description="Customer phone number if provided.")
    complaint_category: str = Field(description="Category such as Billing, Technical, Delivery, Product Defect, or Service.")
    issue_description: str = Field(description="Concise summary of the core problem described in the document.")
    resolution_provided: str = Field(description="Any resolution already given, or 'None yet' if unresolved.")
    is_complaint: Literal["Yes", "No"] = Field(description="Whether the document represents an actual complaint.")
    escalation_required: Literal["Yes", "No"] = Field(description="Whether the case requires management or Tier-2 escalation.")
    supporting_document_available: Literal["Yes", "No"] = Field(description="Whether receipts, screenshots, or logs are mentioned/attached.")
    overall_case_status: Literal["Open", "In Progress", "Resolved", "Escalated"] = Field(
        description="Current status of the customer case."
    )
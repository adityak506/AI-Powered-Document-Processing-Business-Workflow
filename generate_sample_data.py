from pathlib import Path
import docx

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def create_txt_samples():
    """Creates realistic .txt complaint and inquiry documents."""
    samples = {
        "complaint_001.txt": (
            "Customer Name: Sarah Jenkins\n"
            "Email: sarah.jenkins@example.com\n"
            "Phone: +1-555-014-8821\n"
            "Date: October 12, 2026\n"
            "Product/Service: CloudSync Pro Subscription\n\n"
            "Issue Details:\n"
            "I was double-charged $49.99 on October 10th for my monthly CloudSync Pro plan. "
            "I contacted live chat yesterday, and Agent Mike confirmed the duplicate transaction "
            "and initiated a refund for one of the charges, which is currently pending.\n\n"
            "Supporting Information:\n"
            "Attached bank statement screenshot showing two identical charges (Transaction IDs #99481 and #99482).\n"
            "Escalation Info: No escalation needed as the refund has already been processed."
        ),
        "complaint_002.txt": (
            "From: Marcus Vance (m.vance@techcorp.io | 555-019-3340)\n"
            "Subject: URGENT - Enterprise API Outage & Data Loss\n\n"
            "Our production environment has been unable to authenticate against your v2 Payment Gateway API "
            "for the past 6 hours. Every request returns a 503 Service Unavailable error. We are losing thousands "
            "of dollars per hour. Tier-1 support told us to clear our cache, which did not resolve anything. "
            "We demand immediate escalation to Senior Engineering and an SLA credit review.\n\n"
            "Supporting Documents: Full server error logs and HAR network traces attached."
        ),
        "complaint_003.txt": (
            "Customer: Priya Nair\n"
            "Contact: priya.nair92@example.org\n"
            "Phone: Not provided\n\n"
            "Message:\n"
            "Hello team, I am not filing a complaint—just wanted to ask if your SmartHome Hub v3 "
            "is compatible with Matter-over-Thread devices out of the box, or if a firmware update is required. "
            "Thanks in advance!"
        ),
    }

    for filename, content in samples.items():
        file_path = DATA_DIR / filename
        file_path.write_text(content, encoding="utf-8")
        print(f"Created: {file_path}")


def create_docx_samples():
    """Creates realistic .docx complaint documents."""
    docx_samples = [
        {
            "filename": "complaint_004.docx",
            "title": "Formal Product Defect Report",
            "paragraphs": [
                "Customer Name: David Morales",
                "Email: dmorales@buildright.com",
                "Phone Number: +1-555-017-6290",
                "Product Involved: AeroBrew Espresso Machine (Model AB-900)",
                "Complaint Description: The steam wand detached during normal operation on the third day of use, causing hot water to leak across my kitchen counter. Luckily no one was burned, but this is a serious safety hazard.",
                "Resolution Provided: None yet. Customer is requesting a full replacement unit or a complete refund.",
                "Escalation Information: Requires immediate Product Safety & Quality Assurance escalation.",
                "Supporting Information: Photos of the detached steam wand and purchase receipt (#INV-77412) are included in the case folder.",
            ],
        },
        {
            "filename": "complaint_005.docx",
            "title": "Delivery Delay Follow-Up",
            "paragraphs": [
                "Customer Name: Elena Rostova",
                "Email: elena.r@example.net",
                "Phone Number: +1-555-011-4099",
                "Order Number: #ORD-55210",
                "Issue Details: My ergonomic office chair was guaranteed for 2-day express delivery, but tracking shows it has been stuck at the regional sorting facility for 5 days.",
                "Resolution Provided: Support waived the $25.00 express shipping fee and issued a 15% discount code for future orders. Package is now out for delivery today.",
                "Escalation Information: None required.",
                "Supporting Information: Carrier tracking log attached.",
            ],
        },
    ]

    for item in docx_samples:
        doc = docx.Document()
        doc.add_heading(item["title"], level=1)
        for p in item["paragraphs"]:
            doc.add_paragraph(p)
        file_path = DATA_DIR / item["filename"]
        doc.save(str(file_path))
        print(f"Created: {file_path}")


if __name__ == "__main__":
    create_txt_samples()
    create_docx_samples()
    print("\nAll sample documents generated successfully in data/!")
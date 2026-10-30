from database import documents
from datetime import datetime, timezone

result = documents.update_one(
    {"file_name": "research_paper.pdf"},
    {
        "$set": {
            "original_name": "research_paper.pdf",
            "updated_at": datetime.now(timezone.utc)
        }
    }
)

if result.matched_count == 1:
    print("Document structure updated successfully!")
else:
    print("Document not found!")
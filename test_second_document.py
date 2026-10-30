from database import users, documents
from datetime import datetime, timezone

user = users.find_one({
    "email": "test@example.com"
})

if user is None:
    print("Test user not found!")

else:
    document = {
        "user_id": user["_id"],
        "original_name": "another_research_paper.pdf",
        "file_name": "another_research_paper.pdf",
        "file_path": "uploads/another_research_paper.pdf",
        "file_type": "pdf",
        "file_size": 198456,
        "page_count": 6,
        "status": "uploaded",
        "uploaded_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    }

    result = documents.insert_one(document)

    print("Second document created successfully!")
    print("Document ID:", result.inserted_id)
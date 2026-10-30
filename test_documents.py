from database import users, documents
from datetime import datetime, timezone

# Find our test user
user = users.find_one({"email": "test@example.com"})

if user is None:
    print("Test user not found!")
else:
    document = {
        "user_id": user["_id"],
        "file_name": "research_paper.pdf",
        "file_path": "uploads/research_paper.pdf",
        "file_type": "pdf",
        "file_size": 245678,
        "page_count": 8,
        "status": "uploaded",
        "uploaded_at": datetime.now(timezone.utc)
    }

    result = documents.insert_one(document)

    print("Document uploaded successfully!")
    print("Document ID:", result.inserted_id)
    print("User ID:", user["_id"])
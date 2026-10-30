from database import users, documents, comparisons
from datetime import datetime, timezone

# Find the test user
user = users.find_one({
    "email": "test@example.com"
})

if user is None:
    print("Test user not found!")

else:
    # Find first document
    document1 = documents.find_one({
        "file_name": "research_paper.pdf",
        "user_id": user["_id"]
    })

    # Find second document
    document2 = documents.find_one({
        "file_name": "another_research_paper.pdf",
        "user_id": user["_id"]
    })

    if document1 is None or document2 is None:
        print("One or both documents were not found!")

    else:
        comparison = {
            "user_id": user["_id"],
            "document1_id": document1["_id"],
            "document2_id": document2["_id"],
            "status": "completed",
            "created_at": datetime.now(timezone.utc)
        }

        result = comparisons.insert_one(comparison)

        print("Comparison created successfully!")
        print("Comparison ID:", result.inserted_id)
        print("Document 1:", document1["_id"])
        print("Document 2:", document2["_id"])
from database import users, activity_logs
from datetime import datetime, timezone

# Find our test user
user = users.find_one({
    "email": "test@example.com"
})

if user is None:
    print("Test user not found!")

else:
    activity = {
        "user_id": user["_id"],

        "action": "comparison_completed",

        "description": (
            "Plagiarism comparison completed successfully."
        ),

        "created_at": datetime.now(timezone.utc)
    }

    result = activity_logs.insert_one(activity)

    print("Activity log created successfully!")
    print("Activity ID:", result.inserted_id)
    print("User ID:", user["_id"])
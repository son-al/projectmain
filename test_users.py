from database import users
from datetime import datetime, timezone

user = {
    "name": "Test User",
    "email": "test@example.com",
    "password_hash": "test_password_hash",
    "role": "user",
    "created_at": datetime.now(timezone.utc)
}

result = users.insert_one(user)

print("User created successfully!")
print("User ID:", result.inserted_id)

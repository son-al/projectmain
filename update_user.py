from database import users

result = users.update_one(
    {"email": "test@example.com"},
    {
        "$set": {
            "is_active": True
        }
    }
)

if result.modified_count == 1:
    print("User updated successfully!")
else:
    print("User was not updated.")
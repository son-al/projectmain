from database import user_settings
from bson import ObjectId

user_id = ObjectId("6a927c9db114b5e38eb89808")

duplicate_settings = {
    "user_id": user_id,
    "general": {
        "newsletter_subscribe": True
    },
    "appearance": {
        "font_size": "large",
        "theme": "blue"
    }
}

try:
    user_settings.insert_one(duplicate_settings)
    print("Duplicate settings were inserted.")
except Exception as e:
    print("Duplicate settings prevented successfully!")
    print("Error:", type(e).__name__)
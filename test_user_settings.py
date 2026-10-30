from database import user_settings
from bson import ObjectId
from datetime import datetime, timezone

user_id = ObjectId("6a927c9db114b5e38eb89808")

settings = {
    "user_id": user_id,

    "general": {
        "newsletter_subscribe": False,
        "background_on_close": True,
        "show_in_applications_bar": True,
        "allow_comments": False
    },

    "appearance": {
        "font_size": "medium",
        "theme": "purple"
    },

    "updated_at": datetime.now(timezone.utc)
}

result = user_settings.insert_one(settings)

print("User settings created successfully!")
print("Settings ID:", result.inserted_id)
print("User ID:", user_id)
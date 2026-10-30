from database import user_settings
from bson import ObjectId

user_id = ObjectId("6a927c9db114b5e38eb89808")

settings = user_settings.find_one({
    "user_id": user_id
})

if settings:
    print("User settings found successfully!")
    print("\nSettings details:")

    for key, value in settings.items():
        print(f"{key}: {value}")
else:
    print("User settings not found!")
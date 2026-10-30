from database import user_settings

settings = user_settings.find_one()

if settings:
    print("========== USER SETTINGS CHECK ==========")
    print("Settings ID:", settings["_id"])
    print("User ID:", settings["user_id"])

    print("\nGeneral Settings:")
    for key, value in settings["general"].items():
        print(f"  {key}: {value}")

    print("\nAppearance Settings:")
    for key, value in settings["appearance"].items():
        print(f"  {key}: {value}")

    print("\nUpdated At:", settings["updated_at"])

    print("\nUser settings collection is working correctly!")
else:
    print("No user settings found.")
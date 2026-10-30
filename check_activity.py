from database import activity_logs
from bson import ObjectId

user_id = ObjectId("6a927c9db114b5e38eb89808")

logs = list(activity_logs.find({
    "user_id": user_id
}))

if logs:
    print("Activity logs found successfully!")
    print(f"Number of logs: {len(logs)}")

    for log in logs:
        print("\nActivity:")
        for key, value in log.items():
            print(f"{key}: {value}")
else:
    print("No activity logs found for this user.")
from database import reports
from bson import ObjectId

report = reports.find_one({
    "_id": ObjectId("6aad4b3cb1784e22d0d340e0")
})

if report:
    print("Report found successfully!")
    print("\nReport details:")
    
    for key, value in report.items():
        print(f"{key}: {value}")
else:
    print("Report not found!")
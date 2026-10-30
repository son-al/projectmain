from database import comparisons
from bson import ObjectId
from datetime import datetime, timezone

comparison = comparisons.find_one({
    "document1_id": ObjectId("6a9280ff240b8f984e93856c"),
    "document2_id": ObjectId("6a95a549964953134ee5d832")
})

if comparison is None:
    print("Comparison not found!")

else:
    result = comparisons.update_one(
        {"_id": comparison["_id"]},
        {
            "$set": {
                "status": "completed",
                "completed_at": datetime.now(timezone.utc)
            }
        }
    )

    if result.matched_count == 1:
        print("Comparison updated successfully!")
        print("Comparison ID:", comparison["_id"])
from database import comparisons, reports
from bson import ObjectId
from datetime import datetime, timezone

# Find the correct comparison
comparison = comparisons.find_one({
    "_id": ObjectId("6a95a577348efe398f5ce9a5")
})

if comparison is None:
    print("Correct comparison not found!")

else:
    report = {
        "comparison_id": comparison["_id"],

        "overall_similarity": 74.5,

        "sentence_coverage": 60.2,

        "sentence_similarity": 82.1,

        "ngram_overlap": 41.8,

        "risk_level": "high",

        "analysis": {
            "two_gram": 42.3,
            "three_gram": 41.7,
            "four_gram": 40.9,
            "five_gram": 39.8
        },

        "processing_time": 2.84,

        "created_at": datetime.now(timezone.utc),

        "updated_at": datetime.now(timezone.utc)
    }

    result = reports.insert_one(report)

    print("Correct comparison report created successfully!")
    print("Report ID:", result.inserted_id)
    print("Comparison ID:", comparison["_id"])
    
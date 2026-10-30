from database import comparisons, reports
from datetime import datetime, timezone

# Find the latest comparison
comparison = comparisons.find_one(
    sort=[("_id", -1)]
)

if comparison is None:
    print("No comparison found!")
else:

    report = {
        "comparison_id": comparison["_id"],

        "overall_similarity": 74,

        "sentence_coverage": 60,

        "sentence_similarity": 82,

        "ngram_overlap": 41,

        "risk_level": "High",

        "analysis": {
            "two_gram": 42,
            "three_gram": 41,
            "four_gram": 41,
            "five_gram": 40
        },

        "created_at": datetime.now(timezone.utc)
    }

    result = reports.insert_one(report)

    print("Report created successfully!")
    print("Report ID:", result.inserted_id)
    print("Comparison ID:", comparison["_id"])
from database import matches
from bson import ObjectId
from datetime import datetime, timezone

report_id = ObjectId("6aad4b3cb1784e22d0d340e0")

match = {
    "report_id": report_id,
    "original_text": "Artificial intelligence is changing modern technology.",
    "matched_text": "AI is transforming modern technology.",
    "similarity": 82.5,
    "match_type": "text",
    "severity": "high",
    "source_document": "another_research_paper.pdf",
    "sentence_number": 1,
    "created_at": datetime.now(timezone.utc)
}

result = matches.insert_one(match)

print("Match created successfully!")
print("Match ID:", result.inserted_id)
print("Report ID:", report_id)
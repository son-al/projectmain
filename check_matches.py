from database import matches
from bson import ObjectId

report_id = ObjectId("6aad4b3cb1784e22d0d340e0")

match_list = list(matches.find({
    "report_id": report_id
}))

if match_list:
    print("Matches found successfully!")
    print(f"Number of matches: {len(match_list)}")

    for match in match_list:
        print("\nMatch:")
        for key, value in match.items():
            print(f"{key}: {value}")
else:
    print("No matches found for this report.")
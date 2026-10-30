from database import (
    users,
    documents,
    comparisons,
    reports,
    matches,
    activity_logs
)

collections = {
    "users": users,
    "documents": documents,
    "comparisons": comparisons,
    "reports": reports,
    "matches": matches,
    "activity_logs": activity_logs
}

print("\n========== FINAL DATABASE CHECK ==========\n")

for name, collection in collections.items():
    count = collection.count_documents({})
    print(f"{name}: {count} document(s)")

print("\n========== INDEX CHECK ==========\n")

for name, collection in collections.items():
    indexes = collection.index_information()
    print(f"{name}:")
    
    for index_name in indexes:
        print(f"  - {index_name}")
    
    print()

print("========== DATABASE CHECK COMPLETE ==========")
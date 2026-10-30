from database import db

# Create collections
db.create_collection("users")
db.create_collection("documents")
db.create_collection("comparisons")
db.create_collection("reports")
db.create_collection("matches")
db.create_collection("activity_logs")

print("Database collections created successfully!")

print("\nCollections:")
for collection in db.list_collection_names():
    print("-", collection)
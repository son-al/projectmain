import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["plagiarism_db"]


users = db["users"]
documents = db["documents"]
comparisons = db["comparisons"]
reports = db["reports"]
matches = db["matches"]
activity_logs = db["activity_logs"]
user_settings = db["user_settings"]

users.create_index("email", unique=True)
users.create_index("created_at")

documents.create_index("user_id")
documents.create_index("uploaded_at")

comparisons.create_index("user_id")
comparisons.create_index("document1_id")
comparisons.create_index("document2_id")
comparisons.create_index("created_at")

reports.create_index("comparison_id")
reports.create_index("created_at")


matches.create_index("report_id")
matches.create_index("similarity")
matches.create_index("severity")


activity_logs.create_index("user_id")
activity_logs.create_index("action")
activity_logs.create_index("created_at")

user_settings.create_index("user_id", unique=True)
user_settings.create_index("updated_at")

try:
    client.admin.command("ping")
    print("MongoDB Connected Successfully!")
    print("Database:", db.name)

except Exception as e:
    print("MongoDB Connection Failed!")
    print(e)
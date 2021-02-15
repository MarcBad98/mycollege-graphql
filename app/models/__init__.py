import os

from mongoengine import connect


connect(
    db=os.environ.get("MONGO_SERVICE_DB", "mycollege"),
    host=os.environ.get("MONGO_SERVICE_HOST", "localhost"),
    port=int(os.environ.get("MONGO_SERVICE_PORT", "27017")),
    username=os.environ.get("MONGODB_USERNAME"),
    password=os.environ.get("MONGODB_PASSWORD"),
    authentication_source="admin",
)

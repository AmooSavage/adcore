from pymongo import MongoClient
from bson import ObjectId
from app.config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

# MongoDB Connection
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]


# Helper function to convert MongoDB ObjectId to string
def serialize_id(data):
    if "_id" in data:
        data["_id"] = str(data["_id"])
    return data


# Fetch all payments with optional filters
def fetch_payments(filter_query={}, skip=0, limit=10):
    """
    Fetch payments from MongoDB with optional filters, pagination, and sorting.
    :param filter_query: Dictionary for filtering payments.
    :param skip: Number of records to skip (for pagination).
    :param limit: Maximum number of records to return.
    :return: List of payments.
    """
    payments = collection.find(filter_query).skip(skip).limit(limit)
    return [serialize_id(payment) for payment in payments]


# Insert a new payment
def create_payment(data):
    """
    Insert a new payment into the MongoDB collection.
    :param data: Dictionary containing payment details.
    :return: The inserted payment's ID.
    """
    result = collection.insert_one(data)
    return str(result.inserted_id)


# Update a payment by ID
def update_payment(payment_id, updates):
    """
    Update an existing payment in MongoDB.
    :param payment_id: The MongoDB ObjectId of the payment to update.
    :param updates: Dictionary of fields to update.
    :return: Boolean indicating success.
    """
    result = collection.update_one(
        {"_id": ObjectId(payment_id)}, {"$set": updates}
    )
    return result.modified_count > 0


# Delete a payment by ID
def delete_payment(payment_id):
    """
    Delete a payment from MongoDB by ID.
    :param payment_id: The MongoDB ObjectId of the payment to delete.
    :return: Boolean indicating success.
    """
    result = collection.delete_one({"_id": ObjectId(payment_id)})
    return result.deleted_count > 0


# Count payments (for pagination or statistics)
def count_payments(filter_query={}):
    """
    Count the total number of payments matching a filter.
    :param filter_query: Dictionary for filtering payments.
    :return: Total number of matching payments.
    """
    return collection.count_documents(filter_query)

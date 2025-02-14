from app import app, users_collection
from flask import request, jsonify

@app.route("/home", methods=["GET"])
def home():
    return jsonify({"message": "Hello, World!"})


@app.route("/api/users", methods=["GET"])
def get_users():
    """
    Retrieve all users from the database.
    """
    # users = list(users_collection.find())
    # # Convert ObjectId to string
    # for user in users:
    #     user["_id"] = str(user["_id"])
    # return jsonify(users), 200
    fake_user = {
        "username": "john_doe",
        "password": "hashed_password",
        "roles": ["is_user_admin", "is_user_manager"],
        "preferences": {"timezone": "UTC"},
        "created_ts": 1634330000
    }
    return jsonify([fake_user]), 201


@app.route("/api/users", methods=["POST"])
def create_user():
    """
    Create a new user.
    """
    user_data = request.json
    result = users_collection.insert_one(user_data)
    return jsonify({"inserted_id": str(result.inserted_id)}), 201


@app.route("/api/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Update an existing user by ID.
    """
    update_data = request.json
    result = users_collection.update_one(
        {"_id": user_id},
        {"$set": update_data}
    )
    if result.modified_count == 0:
        return jsonify({"error": "No user updated"}), 404
    return jsonify({"message": "User updated"}), 200


@app.route("/api/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Delete a user by ID.
    """
    result = users_collection.delete_one({"_id": user_id})
    if result.deleted_count == 0:
        return jsonify({"error": "No user deleted"}), 404
    return jsonify({"message": "User deleted"}), 200

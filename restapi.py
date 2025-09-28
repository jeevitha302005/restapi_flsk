from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = {}

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET a single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST: Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": data.get("name"), "email": data.get("email")}
    return jsonify(users[user_id]), 201

# PUT: Update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    if user_id in users:
        users[user_id]["name"] = data.get("name", users[user_id]["name"])
        users[user_id]["email"] = data.get("email", users[user_id]["email"])
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404

# DELETE: Remove a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"message": "User deleted", "user": deleted_user})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

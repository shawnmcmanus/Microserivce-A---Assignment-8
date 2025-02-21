from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

@app.route("/api/auth/encrypt", methods=["POST"])
def encrypt_password():
    data = request.get_json()
    password = data.get("password")

    if not password:
        return jsonify({"error": "Password is required"}), 400
    
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    return jsonify({"hash": hashed_password.decode("utf-8")}), 200

@app.route("/api/auth/verify", methods=["POST"])
def verify_decryption():
    data = request.get_json()
    password = data.get("password")
    stored_hash = data.get("hash")

    if not all([password, stored_hash]):
        return jsonify({"valid": False, "message": "Missing required fields"}), 400
    
    try:
        valid = bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
        return jsonify({"valid": valid, "message": None if valid else "Password does not match"}), 200
    except ValueError:
        return jsonify({"valid": False, "message": "Invalid input format"}), 400
    except Exception:
        return jsonify({"valid": False, "message": "Internal server error"}), 500

if __name__ == "__main__":
    print("Password Encryption and Verification Microservice listening...")
    app.run(host='127.0.0.1', port=8080, debug=True)
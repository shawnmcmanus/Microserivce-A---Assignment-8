import requests

BASE_URL = "http://127.0.0.1:8080/api/auth"

def encrypt(password):
    encrypt_response = requests.post(f"{BASE_URL}/encrypt", json={"password": password})
    print(f"Sending password- {password} for encryption...")

    encrypt_data = encrypt_response.json()
    hashed_password = encrypt_data["hash"]
    print(f"Storing hashed password- {hashed_password}...")
    return hashed_password

def verify(password, hashed_password):
    print("Verifying password...")
    verify_response = requests.post(f"{BASE_URL}/verify", json={
        "password": password,
        "hash": hashed_password
    })

    verify_data = verify_response.json()
    if verify_data["valid"]:
        print("Password is correct!")
    else:
        print(verify_data["message"])


if __name__ == "__main__":
    password = input("Enter your new password: ")
    hashed_password = encrypt(password)
    user_password = input("Enter your password: ")
    verify(user_password, hashed_password)
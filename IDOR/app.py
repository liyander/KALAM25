from flask import Flask, request, redirect

app = Flask(__name__)

users = {
    "1": {"name": "Alice", "email": "alice@example.com"},
    "2": {"name": "Bob", "email": "bob@example.com"},
    "admin": {"name": "Admin", "email": "admin@example.com", "flag": "KALAM25{1D0R_3xpl01t3D}"},
}

@app.route("/")
def home():
    return redirect("/profile?id=1")

@app.route("/profile")
def profile():
    user_id = request.args.get("id", "1")

    if user_id in users:
        user_data = users[user_id]
        response = f"<h2>Profile of {user_data['name']}</h2>"
        response += f"<p>Email: {user_data['email']}</p>"

        if "flag" in user_data:
            response += f"<p>FLAG: {user_data['flag']}</p>"

        return response
    else:
        return "User not found!", 404

if __name__ == "__main__":
    app.run(debug=True)


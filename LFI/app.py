from flask import Flask, request

app = Flask(__name__)

# Allowed files for LFI
ALLOWED_FILES = {
    "../../flag.txt": "flag.txt",
    "../../etc/passwd": "/etc/passwd"
}

@app.route("/")
def home():
    return '''
        <h2>Lot oF Interesting files LOL</h2>
        <form action="/view" method="get">
            <input type="text" name="file" placeholder="Enter file name">
            <button type="submit">View File</button>
        </form>
    '''

@app.route("/view")
def view_file():
    file_key = request.args.get("file", "")

    # Allow only specific files
    if file_key in ALLOWED_FILES:
        try:
            with open(ALLOWED_FILES[file_key], "r") as f:
                content = f.read()
            return f"<pre>{content}</pre>"
        except Exception as e:
            return "Error reading file."
    else:
        return "Access Denied!"

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, request, render_template_string
#{{ cycler.__init__.__globals__.os.popen('cat flag.txt').read() }}
app = Flask(__name__)

FLAG_FILE = "flag.txt"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        template = f"<h1>Welcome, {name}!</h1>"
        return render_template_string(template)

    return '''
    <form method="POST">
        <input type="text" name="name" placeholder="Enter your name">
        <button type="submit">Submit</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        msg = request.form.get("message")

        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(msg + "\n")

        return "Saved Successfully"

    return """
    <h2>Type Anything</h2>
    <form method="post">
        <input type="text" name="message">
        <button type="submit">Submit</button>
    </form>
    """

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
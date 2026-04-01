from flask import Flask, render_template, request,jsonify
import os

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html", name="mark")

@app.route("/run", methods=["POST"])
def call():
    name = request.json.get("name")
    phone = request.json.get("phone")

    return jsonify({
        "name":"new_"+name,
        "phone":"new_"+phone
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
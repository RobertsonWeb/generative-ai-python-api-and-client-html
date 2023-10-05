from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

@app.route("/")
def web_client():
    return render_template('web_client.html')

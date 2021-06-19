from flask import Flask, request
app = Flask(__name__)
import os



@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/failure", methods=['GET', 'POST'])
def save_failed_item():
    url = request.form.get('url')
    print(url)
    with open("failed.plist", "a") as f:
        f.write(url)
        f.write("\n")
    return "ok"
    
    
@app.route("/succeeded", methods= ['GET', 'POST'])
def save_succeeded_item():
    url = request.form.get('url')
    print(url)
    with open("succeeded.plist", "a") as f:
        f.write(url)
        f.write("\n")
    return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8787)

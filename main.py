import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Write your prompto here
    # JSON形式で{"message": "Hello, World!"}というレスポンスを返すコードを生成してください。    
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
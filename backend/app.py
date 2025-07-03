from flask import Flask
from routes.predict import predict_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(predict_bp)

@app.route('/')
def home():
    return "✅ Flask backend for Machine Failure Prediction is running!"


if __name__ == '__main__':
    app.run(debug=True)

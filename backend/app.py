# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Kết nối MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://omron_mongo:27017/")
client = MongoClient(MONGO_URI)
db = client["omron"]
collection = db["sensor"]

@app.route("/api/sensors", methods=["GET"])
def get_sensors():
    try:
        # Lấy 10 document mới nhất
        sensors = collection.find().sort("_id", -1).limit(10)
        response = []
        for sensor in sensors:
            # Loại bỏ trường _id vì MongoDB trả về dạng ObjectId không tương thích
            sensor["_id"] = str(sensor["_id"])
            response.append(sensor)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

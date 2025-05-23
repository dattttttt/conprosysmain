from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Kết nối MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://omron_mongo:27017/omron")
client = MongoClient(MONGO_URI)
db = client["omron"]

@app.route("/api/sensors", methods=["GET"])
def get_sensors():
    try:
        sensors = db["sensor"].find().sort("_id", -1).limit(10)
        response = []
        for sensor in sensors:
            sensor["_id"] = str(sensor["_id"])
            response.append(sensor)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Route động cho từng loại cảm biến (e.g. /api/temperature)
@app.route("/api/<sensor_type>", methods=["GET"])
def get_sensor_by_type(sensor_type):
    try:
        # Chỉ lấy 10 bản ghi mới nhất của sensor_type
        collection = db[sensor_type.lower()]  # ví dụ db["temperature"]
        docs = list(collection.find().sort("timestamp", -1).limit(10))
        for doc in docs:
            doc["_id"] = str(doc["_id"])
        return jsonify(docs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

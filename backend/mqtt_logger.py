# backend/mqtt_logger.py

import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
import os
from datetime import datetime

# Kết nối MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://omron_mongo:27017/omron")
client = MongoClient(MONGO_URI)
db = client["omron"]
collection = db["sensor"]

# Hàm xử lý khi nhận được message
def on_message(client, userdata, message):
    try:
        # Giải mã payload từ thiết bị cảm biến
        payload = json.loads(message.payload.decode())
        
        # Thêm timestamp nếu chưa có
        if "timestamp" not in payload:
            payload["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"Received message: {payload}")

        # Lưu vào MongoDB
        result = collection.insert_one(payload)
        print(f"Đã lưu vào MongoDB: {payload} với _id: {result.inserted_id}")

    except Exception as e:
        print(f"Error processing message: {e}")

# Kết nối tới MQTT broker
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect("omron_mqtt", 1883)
mqtt_client.subscribe("CPS/data")
print("🚀 Đang lắng nghe topic 'CPS/data'...")

mqtt_client.loop_forever()

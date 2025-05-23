import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
import os
from datetime import datetime

# Kết nối MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://omron_mongo:27017/omron")
client = MongoClient(MONGO_URI)
db = client["omron"]

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ MQTT kết nối thành công.")
        client.subscribe("CPS/data")
    else:
        print(f"❌ MQTT lỗi kết nối. Mã: {rc}")

def on_message(client, userdata, message):
    try:
        payload = json.loads(message.payload.decode())
        UUID = payload.get("UUID")
        SN = payload.get("SN")
        T = payload.get("T")
        timestamp = payload.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        for sensor in payload.get("DATA", []):
            sensor_type = sensor.get("NE").lower()  # e.g. "temperature"
            value = sensor.get("V")

            if sensor_type and value is not None:
                doc = {
                    "UUID": UUID,
                    "SN": SN,
                    "T": T,
                    "timestamp": timestamp,
                    "value": value
                }
                db[sensor_type].insert_one(doc)
                print(f"📥 Lưu {sensor_type}: {value} → collection `{sensor_type}`")
            else:
                print("⚠️ Sensor data thiếu trường NE/V, bỏ qua.")

    except Exception as e:
        print(f"❌ Lỗi xử lý message: {e}")

# Khởi tạo client MQTT
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

try:
    mqtt_client.connect("omron_mqtt", 1883)
    print("🚀 Đang lắng nghe topic 'CPS/data'...")
    mqtt_client.loop_forever()
except Exception as e:
    print(f"❌ Lỗi kết nối MQTT: {e}")

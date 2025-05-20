<template>
  <div class="sensor-detail">
    <div class="sensor-circle">
      <div class="sensor-value">{{ sensorValue }}</div>
      <div class="sensor-name">{{ currentSensorType }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['sensorType'],
  data() {
    return {
      currentSensorType: '',
      sensorValue: 0,
      updateInterval: null,
      // Map tên cảm biến từ MongoDB sang frontend
      sensorNameMap: {
        pressure: "AtmosphericPressure",
        discomfort: "DiscomfortIndex",
        heatstroke: "HeatstrokeRiskLevel",
        temperature: "temperature",
        humidity: "Humidity",
        illuminance: "Illuminance",
        noise: "Noise",
        etvoc: "eTVOC",
        eco2: "eCO2"
      }
    };
  },
  watch: {
    sensorType: {
      immediate: true,
      handler(newType) {
        this.currentSensorType = newType;
        this.sensorValue = 0;
        this.startAutoUpdate();
      }
    }
  },
  mounted() {
    this.currentSensorType = this.sensorType;
    this.startAutoUpdate();
  },
  beforeUnmount() {
    this.stopAutoUpdate();
  },
  methods: {
    async fetchSensorData(sensorType) {
      try {
        const response = await fetch(`http://localhost:5000/api/sensors`);
        const data = await response.json();

        // Chuyển đổi tên cảm biến từ frontend sang MongoDB
        const mappedType = this.sensorNameMap[sensorType] || sensorType;

        // Tìm sensor theo loại hiện tại
        const sensor = data[0].DATA.find(item => item.NE === mappedType);
        if (sensor) {
          this.sensorValue = sensor.V;
        } else {
          console.warn(`Không tìm thấy dữ liệu cho loại cảm biến: ${sensorType}`);
        }
      } catch (error) {
        console.error('Error fetching sensor data:', error);
      }
    },
    startAutoUpdate() {
      this.stopAutoUpdate(); // Dừng timer cũ nếu có
      this.fetchSensorData(this.currentSensorType);
      this.updateInterval = setInterval(() => {
        this.fetchSensorData(this.currentSensorType);
      }, 5000);
    },
    stopAutoUpdate() {
      if (this.updateInterval) {
        clearInterval(this.updateInterval);
        this.updateInterval = null;
      }
    }
  }
};
</script>

<style scoped>
.sensor-detail {
  display: flex;
  gap: 30px;
  align-items: center;
}

.sensor-circle {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background-color: #111;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #f0a500;
  font-size: 48px;
  font-weight: bold;
  border: 5px solid #f0a500;
}

.sensor-name {
  font-size: 24px;
  margin-top: 10px;
}
</style>

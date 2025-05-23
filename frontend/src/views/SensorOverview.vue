<template>
  <div class="overview-container">
    <h2 class="title">
      <font-awesome-icon icon="chart-pie" class="icon" />
      <span class="highlight">センサー概要</span>
    </h2>
    <div class="sensor-grid">
      <div
        class="sensor-card"
        v-for="sensor in sensorList"
        :key="sensor.key"
      >
        <h3 class="sensor-name">{{ sensor.label }}</h3>
        <p class="sensor-value">
          {{ formattedValue(sensor.key) }} {{ sensor.unit }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SensorOverview",
  data() {
    return {
      data: {},
      interval: null,
      sensorList: [
        { key: "temperature", label: "温度", unit: "°C" },
        { key: "humidity", label: "湿度", unit: "%" },
        { key: "illuminance", label: "照度", unit: "lx" },
        { key: "atmosphericpressure", label: "気圧", unit: "hPa" },
        { key: "noise", label: "騒音", unit: "dB" },
        { key: "etvoc", label: "TVOC", unit: "ppb" },
        { key: "eco2", label: "CO₂", unit: "ppm" },
        { key: "discomfortindex", label: "不快指数", unit: "" },
        { key: "heatstrokerisklevel", label: "熱中症指数", unit: "" }
      ]
    };
  },
  methods: {
    async fetchData() {
      for (const sensor of this.sensorList) {
        try {
          const res = await fetch(`http://localhost:5000/api/${sensor.key}`);
          const json = await res.json();
          this.data[sensor.key] = json[0]?.value ?? "-";
        } catch (err) {
          console.error(`❌ Lỗi khi lấy ${sensor.key}:`, err);
          this.data[sensor.key] = "Lỗi";
        }
      }
    },
    formattedValue(key) {
      const val = this.data[key];
      if (typeof val === 'number') {
        return Math.round(val);
      }
      return val;
    }
  },
  mounted() {
    this.fetchData();
    this.interval = setInterval(this.fetchData, 5000); // cập nhật mỗi 5s
  },
  beforeUnmount() {
    clearInterval(this.interval);
  }
};
</script>

<style scoped>
.overview-container {
  padding: 24px;
  max-width: 1300px;
  margin: auto;
  color: #f1f1f1;
}

.title {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 32px;
  color: #ffffff;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
}

.highlight {
  color: #00eaff;
}

.icon {
  font-size: 26px;
  color: #00eaff;
}

.sensor-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.sensor-card {
  padding: 16px;
  border-radius: 10px;
  background-color: #2a2a2a;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  text-align: center;
}

.sensor-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 14px rgba(0, 0, 0, 0.35);
}

.sensor-name {
  font-size: 26px;
  margin-bottom: 10px;
  font-weight: bold;
  color: #ffffff;
}

.sensor-value {
  font-size: 40px;
  font-weight: bold;
  color: #00eaff;
}
</style>

<template>
  <div class="sensor-card">
    <div class="circle-outline">
      <span class="value">{{ value }}</span>
    </div>
    <div class="label">
      <font-awesome-icon :icon="iconMap[sensorName]" class="icon" />
      {{ sensorLabel }}
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    sensorName: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      value: "-",
      interval: null,
      labelMap: {
        temperature: "温度",
        humidity: "湿度",
        illuminance: "照度",
        atmosphericpressure: "気圧",
        noise: "騒音",
        etvoc: "TVOC",
        eco2: "CO₂",
        discomfortindex: "不快指数",
        heatstrokerisklevel: "熱中症指数"
      },
      iconMap: {
        temperature: "thermometer-half",
        humidity: "tint",
        illuminance: "lightbulb",
        atmosphericpressure: "gauge",
        noise: "volume-up",
        etvoc: "vial",
        eco2: "cloud",
        discomfortindex: "face-grimace",
        heatstrokerisklevel: "sun"
      }
    };
  },
  computed: {
    sensorLabel() {
      return this.labelMap[this.sensorName] || this.sensorName;
    }
  },
  methods: {
    async fetchValue() {
      try {
        const res = await axios.get(`http://localhost:5000/api/${this.sensorName}`);
        if (Array.isArray(res.data) && res.data.length > 0) {
          this.value = res.data[0].value ?? "-";
        } else {
          this.value = "-";
        }
      } catch (err) {
        console.error(`❌ Lỗi khi lấy dữ liệu: ${this.sensorName}`, err);
        this.value = "Lỗi";
      }
    }
  },
  watch: {
    sensorName: {
      immediate: true,
      handler() {
        this.fetchValue();
      }
    }
  },
  mounted() {
    this.interval = setInterval(this.fetchValue, 5000);
  },
  beforeUnmount() {
    clearInterval(this.interval);
  }
};
</script>

<style scoped>
.sensor-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #2c2c2c;
  border-radius: 16px;
  padding: 32px;
  width: 380px;
  box-shadow: 0 0 25px rgba(0, 255, 255, 0.15);
  transition: transform 0.3s ease;
}

.sensor-card:hover {
  transform: translateY(-6px);
}

.circle-outline {
  width: 300px;
  height: 300px;
  border: 6px solid #00bcd4;
  border-radius: 50%;
  background-color: transparent;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 0 25px rgba(0, 255, 255, 0.3);
}

.value {
  font-size: 60px;
  font-weight: bold;
  color: #00eaff;
}

.label {
  margin-top: 24px;
  font-size: 24px;
  color: #eee;
  text-align: center;
  display: flex;
  align-items: center;
  gap: 10px;
}

.icon {
  font-size: 22px;
  color: #00eaff;
}
</style>

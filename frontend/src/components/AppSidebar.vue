<template>
  <nav class="sidebar">
    <ul>
      <li>
        <router-link to="/" active-class="active">
          <font-awesome-icon icon="chart-pie" class="icon" />
          <span class="label">概要</span>
        </router-link>
      </li>
      <li v-for="sensor in sensorList" :key="sensor.key">
        <router-link :to="'/' + sensor.key" active-class="active">
          <font-awesome-icon :icon="sensor.icon" class="icon" />
          <span class="label">{{ sensor.label }}</span>
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "AppSidebar",
  data() {
    return {
      sensorList: [
        { key: "temperature", icon: "thermometer-half", label: "温度" },
        { key: "humidity", icon: "tint", label: "湿度" },
        { key: "illuminance", icon: "lightbulb", label: "照度" },
        { key: "atmosphericpressure", icon: "gauge", label: "大気圧" },
        { key: "noise", icon: "volume-up", label: "騒音" },
        { key: "etvoc", icon: "vial", label: "TVOC" },
        { key: "eco2", icon: "cloud", label: "CO₂" },
        { key: "discomfortindex", icon: "face-grimace", label: "不快指数" },
        { key: "heatstrokerisklevel", icon: "sun", label: "熱中症指数" }
      ]
    };
  }
};
</script>

<style scoped>
.sidebar {
  width: 320px;
  background-color: #1f1f1f;
  color: #fff;
  height: 100vh;
  padding: 24px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 18px;
}

a {
  color: #ddd;
  text-decoration: none;
  font-size: 18px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 8px;
  transition: background-color 0.2s, color 0.2s;
}

a:hover {
  background-color: #333;
  color: #00bcd4;
}

.router-link-active,
a.active {
  background-color: #00bcd4;
  color: #fff !important;
}

.icon {
  font-size: 20px;
  width: 26px;
  text-align: center;
  transition: transform 0.2s ease, filter 0.2s ease;
}

.router-link-active .icon,
a.active .icon {
  transform: scale(1.4);
  filter: drop-shadow(0 0 4px #fff);
  color: #ffffff;
}
</style>

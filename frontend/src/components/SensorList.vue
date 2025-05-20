<template>
  <div>
    <h2>Sensor Data</h2>
    <ul>
      <li v-for="sensor in sensors" :key="sensor._id">
        <strong>{{ sensor.UUID }}</strong> - {{ sensor.timestamp }}
        <ul>
          <li v-for="data in sensor.DATA" :key="data.ID">
            {{ data.NE }}: {{ data.V }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      sensors: [],
    };
  },
  mounted() {
    this.fetchSensorData();
  },
  methods: {
    async fetchSensorData() {
      try {
        const response = await axios.get("http://localhost:5000/api/sensors");
        this.sensors = response.data;
      } catch (error) {
        console.error("Error fetching sensor data:", error);
      }
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
}
</style>

<template>
  <div>
    <h2>センサーの概要 (Sensor Overview)</h2>
    <table>
      <thead>
        <tr>
          <th>センサー名</th>
          <th>値</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(value, key) in sensorData" :key="key">
          <td>{{ key }}</td>
          <td>{{ value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sensorData: {}
    };
  },
  mounted() {
    this.fetchSensorData();
    setInterval(this.fetchSensorData, 5000);
  },
  beforeRouteEnter(to, from, next) {
    next(vm => vm.fetchSensorData());
  },
  methods: {
    async fetchSensorData() {
      try {
        const response = await fetch('http://localhost:5000/api/sensors');
        const data = await response.json();
        if (data.length > 0) {
          const latestSensor = data[0];
          const parsedData = {};
          latestSensor.DATA.forEach((item) => {
            parsedData[item.NE] = item.V;
          });
          this.sensorData = parsedData;
        }
      } catch (error) {
        console.error('Error fetching sensor data:', error);
      }
    }
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  background-color: #333;
  border-radius: 8px;
  overflow: hidden;
}

table th, table td {
  border: 1px solid #444;
  padding: 20px;
  font-size: 24px;
  font-weight: bold;
  text-align: left;
  color: #fff;
}

table th {
  background-color: #555;
  color: #fff;
  font-weight: bold;
}

table tbody tr:nth-child(even) {
  background-color: #444;
}

table tbody tr:nth-child(odd) {
  background-color: #333;
}
</style>

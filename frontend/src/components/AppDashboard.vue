<template>
  <div class="dashboard">
    <h2>App Dashboard</h2>
    <SensorList />
  </div>
</template>

<script>
import SensorList from "./SensorList.vue";

export default {
  name: "AppDashboard",
  components: {
    SensorList,
  },
};
</script>

<style scoped>
.dashboard {
  flex: 1;
  padding: 20px;
}
</style>

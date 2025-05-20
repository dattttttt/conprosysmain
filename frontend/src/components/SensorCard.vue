<!-- src/components/SensorCard.vue -->
<template>
  <div class="card">
    <h3>{{ title }}</h3>
    <p>{{ value }}</p>
  </div>
</template>

<script>
export default {
  props: ["title", "value"],
};
</script>

<style scoped>
.card {
  background-color: #2E2E2E;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
  transition: transform 0.2s, box-shadow 0.2s;
  color: #ffffff;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(255,215,0,0.4);
}
h3 {
  margin: 0;
  font-size: 1.2em;
  color: #FFD700;
}
p {
  font-size: 2em;
  color: #ffffff;
  margin: 0;
}
</style>

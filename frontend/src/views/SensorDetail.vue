<template>
  <div class="sensor-layout">
    <SensorCard :sensorName="sensorType" />
    <SensorChart :sensorName="sensorType" />
  </div>
</template>

<script>
import SensorCard from '@/components/SensorCard.vue'
import SensorChart from '@/components/SensorChart.vue'

export default {
  props: {
    sensorType: {
      type: String,
      required: true
    }
  },
  components: { SensorCard, SensorChart }
}
</script>

<style scoped>
.sensor-layout {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
}
</style>

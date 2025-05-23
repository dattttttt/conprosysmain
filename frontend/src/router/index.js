import { createRouter, createWebHistory } from 'vue-router'
import SensorOverview from '../views/SensorOverview.vue'
import SensorDetail from '../views/SensorDetail.vue'

const routes = [
  {
    path: '/',
    name: 'Overview',
    component: SensorOverview
  },
  {
    path: '/temperature',
    name: 'Temperature',
    component: SensorDetail,
    props: { sensorType: 'temperature' }
  },
  {
    path: '/humidity',
    name: 'Humidity',
    component: SensorDetail,
    props: { sensorType: 'humidity' }
  },
  {
    path: '/illuminance',
    name: 'Illuminance',
    component: SensorDetail,
    props: { sensorType: 'illuminance' }
  },
  {
    path: '/atmosphericpressure',
    name: 'AtmosphericPressure',
    component: SensorDetail,
    props: { sensorType: 'atmosphericpressure' }
  },
  {
    path: '/noise',
    name: 'Noise',
    component: SensorDetail,
    props: { sensorType: 'noise' }
  },
  {
    path: '/etvoc',
    name: 'eTVOC',
    component: SensorDetail,
    props: { sensorType: 'etvoc' }
  },
  {
    path: '/eco2',
    name: 'eCO2',
    component: SensorDetail,
    props: { sensorType: 'eco2' }
  },
  {
    path: '/discomfortindex',
    name: 'DiscomfortIndex',
    component: SensorDetail,
    props: { sensorType: 'discomfortindex' }
  },
  {
    path: '/heatstrokerisklevel',
    name: 'HeatstrokeRiskLevel',
    component: SensorDetail,
    props: { sensorType: 'heatstrokerisklevel' }
  },
  {
    path: '/:catchAll(.*)',
    redirect: '/'  // fallback nếu URL sai
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

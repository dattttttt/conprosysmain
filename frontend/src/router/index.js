import { createRouter, createWebHistory } from 'vue-router';
import SensorOverview from '../views/SensorOverview.vue';
import SensorDetail from '../views/SensorDetail.vue';

const routes = [
  { path: '/', component: SensorOverview },
  { path: '/temperature', component: SensorDetail, props: { sensorType: 'temperature' } },
  { path: '/humidity', component: SensorDetail, props: { sensorType: 'humidity' } },
  { path: '/illuminance', component: SensorDetail, props: { sensorType: 'illuminance' } },
  { path: '/pressure', component: SensorDetail, props: { sensorType: 'pressure' } },
  { path: '/noise', component: SensorDetail, props: { sensorType: 'noise' } },
  { path: '/etvoc', component: SensorDetail, props: { sensorType: 'etvoc' } },
  { path: '/eco2', component: SensorDetail, props: { sensorType: 'eco2' } },
  { path: '/discomfort', component: SensorDetail, props: { sensorType: 'discomfort' } },
  { path: '/heatstroke', component: SensorDetail, props: { sensorType: 'heatstroke' } }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

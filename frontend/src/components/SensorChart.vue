<template>
  <div class="chart-wrapper">
    <div class="filter-bar">
      <label>期間:</label>
      <select v-model="timeRange" @change="fetchChartData">
        <option value="1m">1分</option>
        <option value="1h">1時間</option>
        <option value="1d">1日</option>
        <option value="1mo">1ヶ月</option>
      </select>
    </div>
    <div class="chart-container">
      <canvas ref="chart"></canvas>
    </div>
  </div>
</template>

<script>
import { onMounted, onBeforeUnmount, ref, watch } from 'vue';
import Chart from 'chart.js/auto';

export default {
  props: {
    sensorName: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const chart = ref(null);
    let chartInstance = null;
    let intervalId = null;
    const timeRange = ref("1h");

    const fetchChartData = async () => {
      try {
        const res = await fetch(`http://localhost:5000/api/${props.sensorName}?range=${timeRange.value}`);
        const data = await res.json();

        // Giới hạn về đúng 10 giá trị đều nhau gần nhất nếu có đủ dữ liệu
        const step = Math.max(1, Math.floor(data.length / 10));
        const trimmedData = data.filter((_, i) => i % step === 0).slice(-10);

        const labels = trimmedData.map(item => {
          const d = new Date(item.timestamp);
          return d.toLocaleTimeString('ja-JP', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        });
        const values = trimmedData.map(item => Math.round(item.value));

        if (chartInstance) {
          chartInstance.data.labels = labels;
          chartInstance.data.datasets[0].data = values;
          chartInstance.update();
          return;
        }

        chartInstance = new Chart(chart.value, {
          type: 'line',
          data: {
            labels,
            datasets: [
              {
                label: props.sensorName,
                data: values,
                borderColor: '#00eaff',
                backgroundColor: 'rgba(0, 234, 255, 0.2)',
                tension: 0.4,
                fill: true,
                pointRadius: 4,
                pointHoverRadius: 6
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
              duration: 1000,
              easing: 'linear'
            },
            interaction: {
              mode: 'index',
              intersect: false
            },
            scales: {
              x: {
                reverse: true,
                ticks: {
                  color: '#fff',
                  font: {
                    size: 12
                  }
                }
              },
              y: {
                ticks: {
                  callback: value => Math.round(value),
                  color: '#fff',
                  font: {
                    size: 12
                  }
                },
                beginAtZero: true
              }
            },
            plugins: {
              legend: {
                labels: {
                  color: '#fff'
                }
              }
            }
          }
        });
      } catch (err) {
        console.error('🔥 Error fetching or updating chart:', err);
      }
    };

    onMounted(() => {
      fetchChartData();
      intervalId = setInterval(fetchChartData, 5000);
    });

    onBeforeUnmount(() => {
      if (chartInstance) {
        chartInstance.destroy();
      }
      if (intervalId) {
        clearInterval(intervalId);
      }
    });

    watch(() => props.sensorName, fetchChartData);

    return {
      chart,
      timeRange,
      fetchChartData
    };
  }
};
</script>

<style scoped>
.chart-wrapper {
  width: 100%;
  max-width: 1000px;
  margin: auto;
}

.filter-bar {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 12px;
  color: #fff;
  gap: 8px;
  align-items: center;
  font-size: 14px;
}

.filter-bar select {
  background: #1e1e1e;
  color: #fff;
  border: 1px solid #555;
  padding: 4px 8px;
  border-radius: 4px;
}

.chart-container {
  width: 100%;
  height: 300px;
  background-color: #2a2a2a;
  border-radius: 10px;
  padding: 16px;
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

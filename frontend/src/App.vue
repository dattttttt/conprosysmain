<template>
  <div id="app">
    <header class="header">
      <h1>TOAMUSEN</h1>
    </header>
    <div class="main-container">
      <aside class="sidebar">
        <ul>
          <li><router-link to="/">📊 概要</router-link></li>
          <li><router-link :to="{ path: '/temperature' }">🌡️ 温度</router-link></li>
          <li><router-link :to="{ path: '/humidity' }">💧 湿度</router-link></li>
          <li><router-link :to="{ path: '/illuminance' }">💡 照度</router-link></li>
          <li><router-link :to="{ path: '/pressure' }">🛠️ 大気圧</router-link></li>
          <li><router-link :to="{ path: '/noise' }">🔊 音</router-link></li>
          <li><router-link :to="{ path: '/etvoc' }">☁️ eTVOC</router-link></li>
          <li><router-link :to="{ path: '/eco2' }">🌀 eCO2</router-link></li>
          <li><router-link :to="{ path: '/discomfort' }">😅 不快感指数</router-link></li>
          <li><router-link :to="{ path: '/heatstroke' }">🥵 熱中症リスクレベル</router-link></li>
        </ul>
      </aside>

      <main class="content">
        <router-view />
      </main>
    </div>
    <footer class="footer">
      <span id="datetime"></span>
    </footer>
  </div>
</template>

<script>
export default {
  mounted() {
    this.updateDateTime();
    setInterval(this.updateDateTime, 1000);
  },
  methods: {
    updateDateTime() {
      const now = new Date();
      const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      };
      document.getElementById('datetime').textContent = now.toLocaleString('ja-JP', options);
    }
  }
};
</script>

<style scoped>
body, html {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  width: 100%;
  height: 100%;
  background-color: #222;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background-color: #222;
  color: #fff;
  width: 100%;
}

.header {
  background-color: #333;
  color: #fff;
  padding: 20px;
  text-align: center;
  font-size: 36px;
  font-weight: bold;
}

.main-container {
  display: flex;
  flex: 1;
}

.sidebar {
  width: 300px;
  background-color: #333;
  color: #fff;
  padding: 20px;
  min-height: calc(100vh - 80px);
}

.sidebar ul {
  list-style: none;
  padding: 0;
}

.sidebar ul li {
  margin-bottom: 15px;
}

.sidebar ul li a {
  color: #fff;
  text-decoration: none;
  font-size: 20px;
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: #444;
  border-radius: 8px;
}

.sidebar ul li a:hover {
  background-color: #555;
  color: #00bcd4;
}

.content {
  flex: 1;
  padding: 20px;
  background-color: #1e1e1e;
  border-radius: 10px;
  margin: 0;
  min-height: calc(100vh - 80px);
}

.footer {
  background-color: #333;
  color: #fff;
  padding: 20px;
  text-align: center;
  font-size: 24px;
  font-weight: bold;
  margin-top: auto;
}
</style>

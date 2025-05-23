<template>
  <div id="app">
    <header class="header">
      <h1>TOAMUSEN</h1>
    </header>
    <div class="main-container">
      <AppSidebar />
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
import AppSidebar from './components/AppSidebar.vue';

export default {
  components: {
    AppSidebar
  },
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
  background: linear-gradient(to right, #00bcd4, #005f73);
  color: #fff;
  padding: 6px 10px;
  text-align: center;
  font-size: 26px;
  font-weight: bold;
  letter-spacing: 2px;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.25);
  animation: fadeInDown 0.6s ease-out;
  flex-shrink: 0;
}

.main-container {
  display: flex;
  flex: 1;
  overflow: hidden;
  min-height: 0;
}

.content {
  flex: 1;
  padding: 16px;
  background-color: #1e1e1e;
  border-radius: 8px;
  margin: 0;
  min-height: 0;
  overflow-y: auto;
}

.footer {
  background: linear-gradient(to right, #005f73, #00bcd4);
  color: #fff;
  padding: 14px 24px;
  text-align: center;
  font-size: 22px;
  font-weight: bold;
  box-shadow: 0 -3px 8px rgba(0, 0, 0, 0.25);
  animation: fadeInUp 0.6s ease-out;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 100;
}

.main-container {
  padding-bottom: 60px;
  /* đảm bảo nội dung không bị footer che */
}

@keyframes fadeInDown {
  from {
    transform: translateY(-30%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes fadeInUp {
  from {
    transform: translateY(30%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
</style>

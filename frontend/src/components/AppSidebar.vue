<template>
  <nav class="sidebar">
    <ul>
      <li><router-link to="/">Dashboard</router-link></li>
      <li><router-link to="/overview">Sensor Overview</router-link></li>
      <li><router-link to="/details">Sensor Details</router-link></li>
    </ul>
  </nav>
</template>

<style scoped>
.sidebar {
  width: 250px;
  background-color: #333;
  color: #fff;
  height: 100vh;
  padding: 20px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin-bottom: 15px;
}
a {
  color: #fff;
  text-decoration: none;
}
a:hover {
  color: #00bcd4;
}
</style>

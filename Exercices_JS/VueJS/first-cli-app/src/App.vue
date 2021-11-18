<script>
import Navlink from './components/Navlink.vue'

export default {
  name: 'App',
  components: {
    Navlink
  }
}
</script>

<template>
  <div id="app">
    <nav>
      <Navlink url='/' text="Accueil" />
      <Navlink url='/about' text="A propos" />
      <Navlink url='/contact' text="Contact" />
    </nav>
    <p>Bienvenue sur notre page d'<Navlink url="/" text="Accueil" /></p>
  </div>
</template>

<style lang="scss">
template, body {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  height: 100vh;
  margin: 0;
  padding: 0;
  background: #8cbff1;

}
a {
  text-decoration: none;
  color: lightgray;
}
nav {
  display: flex;
  height: 35px;
  justify-content: space-evenly;
  align-items: center;
  font-size: 1.3em;
  color: white;
  background:linear-gradient(darkBlue,cyan);
}
p > a{
  color: rgb(73, 73, 73);
}
</style>

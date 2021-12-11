import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    bgds: [
      {id: 1, url: "../../public/images/autumn.jpg"},
      {id: 2, url: "../../public/images/biches.jpg"},
      {id: 3, url: "../../public/images/ecureuil.jpg"},
      {id: 4, url: "../../public/images/grenouille.jpg"},
      {id: 5, url: "../../public/images/oiseau.jpg"},
      {id: 6, url: "../../public/images/ours.jpg"},
      {id: 7, url: "../../public/images/ratons.jpg"},
      {id: 8, url: "../../public/images/renards.jpg"},
    ],
      background: "../../public/images/autumn.jpg",
      colorRed: 'red',

  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})

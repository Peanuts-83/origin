import { createStore } from 'vuex'

export default createStore({
  state: {
    backgrounds: [],
    USER_TOUCH: false,
    navWidth: {w0: '25%', w1: '200px', w2: '0'},
    navLevel: 0,
    navSection: 'Home',
    navSec: {
      Production: [
        {name: 'API météo', url: 'https://apimeteo.web.app/'},
        {name: 'Splah site / Bootstrap', url: 'https://splashsite-ae305.web.app/index.html'},
        {name: 'Bibliothèque / webApp', url: 'https://firstproject-aa4fd.web.app/books'},
      ],
      Skills: [
        {name: 'Vue.js', url:''},
        {name: 'Progressive Web App', url:''},
        {name: 'Bootstrap', url:''},
        {name: 'GitHub', url:''},
        {name: 'Docker', url:''},
        {name: 'Databases SQL/NoSQL', url:''},
        {name: 'Node.js', url:''},
        {name: 'Certifications', url:''},
      ]
    },
    mouseX: 0,
    navShow: false,
    target: '',
    specs: {
      xPos: 0,
      info: 0,
      routerWidth: 0,
      routerHeight: 0,
      iframeWidth: 0,
      iframeHeight: 0,
    },

  },
  beforeMount() {
    // TODO: Preload BG Image

  },
  getters: {
    // Choose random bg image
    setBg(state) {
      const bg = require.context(
        '@/assets/images/bgds',
          true,
          /^.*\.jpg$/
      )
      state.backgrounds = bg.keys().map(key => bg(key));
      let index = Math.round(Math.random() * state.backgrounds.length);
      return state.backgrounds[index];
    },
  },
  mutations: {
    DETECT_TOUCH(state) {
      state.USER_TOUCH = true;
    },
    NAV_SECTION(state, name) {
      state.navSection = name;
    },
    NAV_STATE(state, level) {
      state.navLevel = level;
      switch (level) {
        // Nav level 1
        case 1:
          state.navWidth = {w0: '15%', w1: '200px', w2: '200px'};
          break;
        // Nav level 3 showTime with Menu
        case 2:
          state.navWidth = {w0: '1%', w1: '50px', w2: '200px'};
          break;
        // Nav Level 4 without menu
        case 3:
          state.navWidth = {w0: '1%', w1: '50px', w2: '0'};
          break;
        // Nav level 0 HomePage
        default:
          state.navWidth = {w0: '25%', w1: '200px', w2: '0'};
          break;
      }
    },
    X_MOUSE(state, num) {
      if (state.USER_TOUCH) return;
      state.mouseX = num;
      const showingZone = parseInt(state.navWidth.w2) + 70;
      // console.log('SHOWING_ZONE', showingZone, ' NAV_LEVEL', state.navLevel);
      if (state.navLevel == 2 && state.mouseX < showingZone) {
        state.navShow = true;
      } else {
        state.navShow = false;
      }
    },
    TARGET_URL(state, tgt) {
      state.target = tgt;
      console.log('TARGET',state.target);
      if (tgt === '') {
        console.log('SET SPECS TO 0')
        state.specs = {
          xPos: 0,
          info: 0,
          routerWidth: 0,
          routerHeight: 0,
          iframeWidth: 0,
          iframeHeight: 0,
        };
      }
    },
    TOGGLE_NAV(state) {
      state.navShow = !state.navShow;
      console.log('navShow = ', state.navShow);
    },
    ROUTER_SPECS(state) {
      const windowWidth = window.innerWidth;
      // const windowHeight = window.innerHeight;
      const set0 = Math.round(parseInt(state.navWidth.w0) * windowWidth / 100);
      const set1 = parseInt(state.navWidth.w1);

      state.specs = {
        xPos: set0 + set1 + 'px',
        info: '30%',
        routerWidth: '100%',
        routerHeight: '100vh',
        iframeWidth: '100%',
        iframeHeight: '100%',
      };
      console.log('ROUTER_SPECS',state.specs);
    },
  },
  actions: {
    detectUserTouch(context) {
      console.log('TOUCH DETECTED!');
      context.commit('DETECT_TOUCH');
    },
    activateNav(context, payload) {
      context.commit('NAV_SECTION', payload.section);
      context.commit('NAV_STATE', payload.level);
    },
    xCoords(context, payload) {
      // console.log('xCOORDS', payload.x);
      context.commit('X_MOUSE', payload.x);
    },
    setTarget(context, payload) {
      // console.log('PAYLOAD',payload);
      context.commit('TARGET_URL', payload);
    },
    setRouter(context) {
      // console.log('PAYLOAD',payload);
      context.commit('ROUTER_SPECS');
    },
    toggleNavSec(context) {
      console.log('TOGGLING');
      context.commit('TOGGLE_NAV');
    }
  },
  modules: {
  }
})

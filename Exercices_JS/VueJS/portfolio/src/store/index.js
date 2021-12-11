import { createStore } from 'vuex';
import Content from '../assets/content.json';

export default createStore({
  state: {
    backgrounds: [],
    bgImg: false,
    USER_TOUCH: false,
    navWidth: {w0: '25%', w1: '200px', w2: '0'},
    navLevel: 0,
    navSection: 'Home',
    navData: Content,
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
  getters: {
    setBg(state) {
      if (state.bgImg) return;
      const bg = require.context(
        '@/assets/images/bgds',
          true,
          /^.*\.jpg$/
      )
      state.backgrounds =  bg.keys().map(key => bg(key));
      let index = Math.round(Math.random() * state.backgrounds.length) -1;
      index >= 0 ? index : index = 0;

      function preload(array, i) {
        let img = new Image;
        img.src = array[i];
        state.bgImg = `url("${img.src}")`
        console.log('BACKGROUND', state.bgImg);
        array.forEach((image,i, arr) => {
          let img = new Image;
          img.src = arr[i];
          console.log('BG PRELOADED', img);
        });
      }

      preload(state.backgrounds, index);
      // const background = state.backgrounds[index];
      // state.bgImg = `url('${background}')`;


    },
  },
  mutations: {
    // @ setBg
    BACKGROUND_IMG(state) {
      if (state.bgImg) return;
      const bg = require.context(
        '@/assets/images/bgds',
          true,
          /^.*\.jpg$/
      )
      state.backgrounds =  bg.keys().map(key => bg(key));
      let index = Math.round(Math.random() * state.backgrounds.length) -1;
      index >= 0 ? index : index = 0;

      function preload(array, i) {
        let img = new Image;
        img.src = array[i];
        console.log('BACKGROUND', img);
      }

      preload(state.backgrounds, index);
      const background = state.backgrounds[index];
      state.bgImg = `url('${background}')`;
    },
    // @ detectUserTouch()
    DETECT_TOUCH(state) {
      state.USER_TOUCH = true;
    },
    // @ activateNav()
    NAV_SECTION(state, name) {
      state.navSection = name;
      console.log('ACTIVATE_NAV1')
    },
    // @ activateNav()
    NAV_STATE(state, level) {
      state.navLevel = level;
      console.log('ACTIVATE_NAV2')
      switch (level) {
        // Nav level 1
        case 1:
          state.navWidth = {w0: '15%', w1: '200px', w2: '200px'};
          console.log('LEVEL1')
          break;
          // Nav level 2 showTime with Menu
          case 2:
            state.navWidth = {w0: '0%', w1: '50px', w2: '200px'};
            console.log('LEVEL2')
            break;
            // Nav Level 3 without menu
            case 3:
              state.navWidth = {w0: '0%', w1: '50px', w2: '0'};
              console.log('LEVEL3')
              break;
              // Nav level 0 HomePage
              default:
                state.navWidth = {w0: '25%', w1: '200px', w2: '0'};
                console.log('LEVEL0')
          break;
      }
    },
    // @ xCoords()
    X_MOUSE(state, num) {
      if (state.USER_TOUCH) return;   // no mouse detection for @mouseover if touch screen
      if (state.navLevel < 2) return;
      state.mouseX = num;
      const showingZone = 70;
      // console.log('SHOWING_ZONE', showingZone, ' NAV_LEVEL', state.navLevel);
      if (state.mouseX < showingZone ) {
        state.navShow = true;
        state.navLevel = 2;
      } else if (state.mouseX > parseInt(state.navWidth.w2)) {
        state.navShow = false;
        state.navLevel = 3;
      }
    },
    // @ setTarget()
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
    // @ togglenavData() for touch screens
    TOGGLE_NAV(state) {
      state.navShow = !state.navShow;
      // console.log('navShow = ', state.navShow);
    },
    // @ setRouter
    ROUTER_SPECS(state) {
      const windowWidth = window.innerWidth;
      // const windowHeight = window.innerHeight;
      const set0 = Math.round(parseInt(state.navWidth.w0) * windowWidth / 100);
      const set1 = parseInt(state.navWidth.w1);
      console.log('SET0', set0, 'SET1', set1)
      state.specs = {
        xPos: set1 + 'px',
        info: '30%',
        routerWidth: '100%',
        routerHeight: '100vh',
        iframeWidth: '100%',
        iframeHeight: '100%',
      };
      console.log('ROUTER_SPECS',state.specs);
    },
    // @ setIFrame
    IFRAME_CHANGER(state, data) {
      const width = data.width;
      const height = data.height;
      state.specs.iframeWidth = width;
      state.specs.iframeHeight = height;
      console.log('IFRAME CHANGED', state.specs);
    }
  },
  actions: {
    setBg(context) {
      console.log('BG SETTING');
      context.commit('BACKGROUND_IMG');
    },
    detectUserTouch(context) {
      // console.log('TOUCH DETECTED!');
      context.commit('DETECT_TOUCH');
    },
    activateNav(context, payload) {
      // console.log('navLevel', payload)
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
    togglenavData(context) {
      // console.log('TOGGLING');
      context.commit('TOGGLE_NAV');
    },
    setIFrame(context, payload) {
      // console.log('IFRAME NEW DATA',payload);
      context.commit('IFRAME_CHANGER', payload);
    }
  },
  modules: {
  }
})

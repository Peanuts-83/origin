import { createStore } from "redux";

// le state
const initialState = {
    player1: 0,
    player2: 0,
    advantage: null,
    winner: null,
    playing: true,
}

// les actions
export const playpause = () => ({ type: 'playpause' })

export const restart = () => ({ type: 'restart' })

export const setPoint = (player) => ({
        type: 'setPoint',
        payload: { player: player }
    })

// le reducer
function reducer(state = initialState, action) {
    if (action.type === "playpause") {
        return {
            ...state,
            playing: !state.playing,
        }
    }
    if (action.type === 'restart') {
        return initialState

    }
    if (action.type === "setPoint") {
        if (state.playing === false) return state
        const player = action.payload.player
        const other = Object.keys(state).filter(key => key.includes('player') && key !== player)[0]


        if (state.winner === null) {
            switch (state[player]) {
                case 0:
                case 15:
                    return {
                        ...state,
                        [player]: state[player] + 15
                    }

                case 30:
                    return {
                        ...state,
                        [player]: state[player] + 10
                    }

                case 40:
                    if (state[other] === 40) {
                        if (state.advantage === null) {
                            return {
                                ...state,
                                advantage: player
                            }
                        } else {
                            return state.advantage === player ? { ...state, winner: player } : { ...state, advantage: null }
                        }
                    } else {
                        return {
                            ...state,
                            winner: player
                        }
                    }

                default:
                    return state
            }

        }
    }
    return state
}


// le store
export const store = createStore(reducer)

import { useSelector } from "react-redux"

export default function Display() {
    const playing = useSelector(state => state.playing)
    const winner = useSelector(state => state.winner)
    const player1Score = useSelector(state => state.player1)
    const player2Score = useSelector(state => state.player2)
    const advantage = useSelector(state => state.advantage)

    /**
     * Met à jour le text qui affiche le score
     * @param {boolean} playing
     * @param {'player1' | 'player2'} winner
     * @param {number} player1Score
     * @param {number} player2Score
     * @param {'player1' | 'player2'} advantage
     */

    if (winner) {
        if (winner === "player1") {
            return <p className="display">Joueur 1 gagne</p>;
        } else {
            return <p className="display">Joueur 2 gagne</p>;
        }
    } else if (playing === false) {
        return <p className="display">C'est la pause</p>;
    } else {
        let text = "Le score est: " + player1Score + " - " + player2Score;
        if (advantage) {
            if (advantage === "player1") {
                text += " avantage joueur 1";
            } else {
                text += " avantage joueur 2";
            }
        }
        return <p className="display">{text}</p>;

    }


    // return (
    //     <p className="display">Le score est: 0 - 0</p>
    // )
}
import { useDispatch } from "react-redux";
import { playpause } from "../app/store";

export default function PlaypauseButton() {
    const dispatch = useDispatch()

    return(
        <button
            className="button"
            onClick={() => {
                dispatch(playpause())
            }}
        >Pause / Reprendre</button>
    )
}
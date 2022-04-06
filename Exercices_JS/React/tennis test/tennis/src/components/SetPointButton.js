import { useDispatch } from "react-redux";
import { setPoint } from "../app/store";

export default function SetPointButton({player, children}) {
    const dispatch = useDispatch()

    return(
        <button
            className="button"
            onClick={() => {
                console.log('Click', player)
                dispatch(setPoint(player))
            }}
        >{children}</button>
    )
}
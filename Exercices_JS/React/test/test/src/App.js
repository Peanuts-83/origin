import Compteur from './components/Compteur'
import './App.css';
import { useState } from 'react';

function useToggle(initState = true) {
  const [state, toggleState] = useState(initState)

  function toggle() {
    toggleState(s => !s)
  }

  return [
    state,
    toggle
  ]
}


function App() {
  const [compteur, setCompteur] = useToggle(true)

  return (
    <div className="App">
      Afficher le compteur <input type="checkbox" onChange={setCompteur} checked={compteur} /><br />
      {compteur && <Compteur />}
    </div>
  );
}

export default App;

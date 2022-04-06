import '../style/App.css';
import SetPointButton from '../components/SetPointButton';
import ResetButton from '../components/ResetButton';
import PlaypauseButton from '../components/PlaypauseButton';
import Display from '../components/Display';

function App() {

  return (
    <div className="App">
      <Display />
      <div className="buttons">
        <div className="buttons-row">
          <SetPointButton player="player1">Point joueur 1</SetPointButton>
          <SetPointButton player="player2">Point joueur 2</SetPointButton>
        </div>
        <div className="buttons-row">
          <ResetButton />
          <PlaypauseButton />
        </div>
      </div>
    </div>
  );
}

export default App;

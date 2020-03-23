import React, { Component } from "react";
import GetSavedWavesUseCase from "../useCases/GetSavedWavesUseCase";
import NoWavesComponent from "./NoWavesComponent";
import SavedWaveComponent from "./SavedWaveComponent";

class Menu extends Component {
  constructor(props){
    super(props);

    this.state = {
      savedWaves: [],
    } 

    this._showInicio = this._showInicio.bind(this);
    this._renderSavedWaves = this._renderSavedWaves.bind(this);
  }


  _showInicio() {
    const getSavedWavesUseCase = new GetSavedWavesUseCase(); 
    getSavedWavesUseCase.run()
      .then(() => {
        const savedWaves = getSavedWavesUseCase.getSavedWaves();
        this.setState({savedWaves: savedWaves});
      });
  }

  _renderSavedWaves() {
    const { savedWaves } = this.state;

    if (savedWaves.length === 0) {
        return <NoWavesComponent />;
    }

    return savedWaves.map(({
        id, muscle, rms, raw, avgRms, mvc, historicMvc
    }) => (
        <SavedWaveComponent
            id={id}
            muscle={muscle}
            rms={rms}
            raw={raw}
            avgRms={avgRms}
            mvc={mvc}
            historicMvc={historicMvc}
        />
    ));
  }

  render() {
    return (
      <header className='header'>
        <nav>
            <ul className='ul-menu'>
                <li>
                    <a onClick={this._showInicio}>Inicio</a>
                </li>
                <li>
                    <a>Estadísticas</a>
                </li>
            </ul>
        </nav>
        <div className="waves-container">
          {this._renderSavedWaves()}
        </div>
      </header>
    );
  }
}

export default Menu;

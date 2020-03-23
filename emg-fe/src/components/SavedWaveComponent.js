import React, { Component } from "react";
import PropTypes from 'prop-types';
import ChartComponent from "./ChartComponent";


class SavedWaveComponent extends Component{
    constructor(props){
        super(props);

        this.state = {
            parsedMuscle: null,
        };


        this._parseMuscleName = this._parseMuscleName.bind(this);
    }

    componentDidMount() {
        this._parseMuscleName();
    }

    _parseMuscleName(){
        const { muscle } = this.props;

        const parsedMuscle = muscle.split('_')[1];
        this.setState({ parsedMuscle: parsedMuscle });
    }

    render() {
        const { id, rms, raw, avgRms, mvc, historicMvc } = this.props;
        const { parsedMuscle } = this.state;

        return (
            <div className="wave-card">
                <div className="wave-title bubble">
                    <p className="wave-info-title">PACIENTE {id}</p>
                </div>
                <div className="wave-info bubble">
                    <ul>
                        <li><span className='wave-field'>Nombre del músculo: </span>{parsedMuscle}</li>
                        <li><span className='wave-field'>RMS medio: </span>{avgRms} </li>
                        <li><span className='wave-field'>Máxima contracción voluntaria: </span>{mvc} </li>
                        <li><span className='wave-field'>Máxima contracción voluntaria histórica: </span>{historicMvc} </li>
                    </ul>
                </div>
                <ChartComponent title="RMS" data={rms} />
            </div>
        )
    }
}
export default SavedWaveComponent

SavedWaveComponent.propTypes = {
    id: PropTypes.number.isRequired,
    muscle: PropTypes.string.isRequired,
    rms: PropTypes.array.isRequired,
    raw: PropTypes.array.isRequired,
    avgRms: PropTypes.number.isRequired,
    mvc: PropTypes.number.isRequired,
    historicMvc: PropTypes.number.isRequired,
}
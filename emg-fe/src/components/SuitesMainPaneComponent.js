import React, { Component } from "react";
import Spinner from "react-bootstrap/Spinner";
import PropTypes from 'prop-types';
import UserEntity from "../entities/UserEntity";
import GetAllSuitesUseCase from "../useCases/GetAllSuitesUseCase";
import SuiteComponent from "./SuiteComponent";


class SuitesMainPaneComponent extends Component{
    constructor(props){
        super(props);

        this.state = {
            suites: null,
            loading: false,
        };
    }

    componentDidMount() {
        const { userEntity } = this.props;
        this.setState({ loading: true });
        const getAllSuitesUseCase = new GetAllSuitesUseCase(userEntity.userId);
        getAllSuitesUseCase.run()
        .then(() => {
            const suites = getAllSuitesUseCase.getResult();
            this.setState({ suites: suites, loading:false });
        });
    }

    _renderSuites() {
        const { loading, suites } = this.state;
        if( loading ){
            return (
                <Spinner animation="border" role="status">
                    <span className="sr-only">Loading...</span>
                </Spinner>
            )
        }
        if (suites === null && loading) {
            return(
                <p>No tienes pruebas, importa una desde 'Datos'</p>
            )
        }
        if (suites !== null && loading === false)
        {
            const renderedSuites = suites.map((suite, key) =>
                <SuiteComponent key={key} suiteEntity={suite} />
            );
            return(
                <ul className='suite-ul'>
                    { renderedSuites }
                </ul>
            );

        }
    }


    render() {
        

        return (
            <div className="main-pane">
                <div className="informative-main-pane-header">
                    Data
                </div>
                <div className='informative-main-pane-message'>
                    {this._renderSuites()}
                </div>
            </div>
        )
    }
}
export default SuitesMainPaneComponent

SuitesMainPaneComponent.propTypes = {
    userEntity: PropTypes.instanceOf(UserEntity),
}

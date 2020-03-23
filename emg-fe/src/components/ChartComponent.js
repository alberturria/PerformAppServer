import React, { Component } from "react";
import PropTypes from 'prop-types';
import CanvasJSReact from "../canvasjs.react"
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
class ChartComponent extends Component {
    constructor(props){
        super(props);
        
        this.state = {
            dataPoints: null,
        }

        this._parseData = this._parseData.bind(this);
    }

    componentDidMount(){
        this._parseData();
    }

    _parseData() {
        const { data } = this.props;

        const parsedData = [];

        for (let index = 0; index < data.length; index +=1 ){
            const tuple = {x: index, y: data[index]};

            parsedData.push(tuple);
        }

        this.setState({
            dataPoints: parsedData,
        });
    }

	render() {

        const { dataPoints } = this.state;
        const { title } = this.props;

		const options = {
            animationEnabled: true,
            animationDuration: 2000,
            zoomEnabled: true,
            backgroundColor: "#F5F5DC",
			title:{
				text: title
			},
			axisX: {
				
			},
			axisY: {
				title: "Amplitud (µV)",
				includeZero: false
			},
			data: [{
				yValueFormatString: "#,###",
				xValueFormatString: "#(s)",
				type: "spline",
				dataPoints: dataPoints
			}]
		}
		return (
		<div>
			<CanvasJSChart options = {options} />
		</div>
		);
	}
}
export default ChartComponent;

ChartComponent.propTypes = {
    title: PropTypes.string.isRequired,
    data: PropTypes.array.isRequired,
}

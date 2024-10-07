import React from 'react';
import { Bar } from 'react-chartjs-2';

const PriceChart = ({ data }) => {
    return <Bar data={data} />;
};

export default PriceChart;
import React from 'react';
import { VegaLite } from 'react-vega';

const LineChart = () => {
  const spec = {
    $schema: 'https://vega.github.io/schema/vega-lite/v5.json',
    description: 'A simple line chart example.',
    data: {
      values: [
        { x: 1, y: 3 },
        { x: 2, y: 7 },
        { x: 3, y: 5 },
        { x: 4, y: 8 },
        { x: 5, y: 6 },
      ],
    },
    mark: 'line',
    encoding: {
      x: { field: 'x', type: 'quantitative', title: 'The X Axis' },
      y: { field: 'y', type: 'quantitative', title: 'The other Axis, DUH!' },
    },
  };

  return <VegaLite spec={spec} />;
};

export default LineChart;
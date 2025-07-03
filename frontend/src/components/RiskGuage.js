import React from 'react';
import Plot from 'react-plotly.js';

const RiskGauge = ({ value }) => (
  <Plot
    data={[{
      type: 'indicator',
      mode: 'gauge+number',
      value: value,
      title: { text: "Failure Risk %" },
      gauge: {
        axis: { range: [0, 100] },
        bar: { color: "black" },
        steps: [
          { range: [0, 40], color: "green" },
          { range: [40, 75], color: "yellow" },
          { range: [75, 90], color: "orange" },
          { range: [90, 100], color: "red" }
        ],
        threshold: {
          line: { color: "red", width: 4 },
          thickness: 0.75,
          value: value
        }
      }
    }]}
    layout={{ width: 400, height: 300 }}
  />
);

export default RiskGauge;

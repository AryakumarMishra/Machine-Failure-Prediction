import React, { useState } from 'react';
import { Form, Button, Card, Alert, Row, Col } from 'react-bootstrap';
import { predictFailure } from '../utils/api';
import RiskGauge from './RiskGuage';
import Plot from 'react-plotly.js';

const PredictionForm = () => {
  const [inputData, setInputData] = useState({
    air_temp: 298.0,
    process_temp: 308.0,
    speed: 1500.0,
    torque: 40.0,
    tool_wear: 0.0,
    product_quality: 'M',
  });

  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
  const { name, value } = e.target;
  const numericFields = ['air_temp', 'process_temp', 'speed', 'torque', 'tool_wear'];

  setInputData({
        ...inputData,
        [name]: numericFields.includes(name) ? parseFloat(value) : value
    });
    };


  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    try {
      const res = await predictFailure(inputData);
      setResult(res.data);
    } catch (err) {
      setError('Something went wrong. Please try again.');
      console.error(err);
    }
  };

  return (
    <Card className="p-4 shadow-sm">
      <h3 className="mb-4 text-center">🛠️ Machine Failure Prediction</h3>
      <Form onSubmit={handleSubmit}>
        <Row>
          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Air Temperature (K)</Form.Label>
              <Form.Control type="number" step="0.1" name="air_temp" value={inputData.air_temp} onChange={handleChange} />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Rotational Speed (rpm)</Form.Label>
              <Form.Control type="number" name="speed" value={inputData.speed} onChange={handleChange} />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Tool Wear (min)</Form.Label>
              <Form.Control type="number" name="tool_wear" value={inputData.tool_wear} onChange={handleChange} />
            </Form.Group>
          </Col>

          <Col md={6}>
            <Form.Group className="mb-3">
              <Form.Label>Process Temperature (K)</Form.Label>
              <Form.Control type="number" step="0.1" name="process_temp" value={inputData.process_temp} onChange={handleChange} />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Torque (Nm)</Form.Label>
              <Form.Control type="number" step="0.1" name="torque" value={inputData.torque} onChange={handleChange} />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Product Quality</Form.Label>
              <Form.Select name="product_quality" value={inputData.product_quality} onChange={handleChange}>
                <option value="L">L</option>
                <option value="M">M</option>
                <option value="H">H</option>
              </Form.Select>
            </Form.Group>
          </Col>
        </Row>

        <Button variant="primary" type="submit" className="w-100 mt-2">Predict</Button>
      </Form>

      {error && <Alert variant="danger" className="mt-3">{error}</Alert>}

      {result && (
        <div className="mt-4">
          <h5>Failure Probability: {result.probability}</h5>
          <Alert variant={
            result.risk_level === 'Low' ? 'success' :
            result.risk_level === 'Moderate' ? 'warning' :
            result.risk_level === 'High' ? 'danger' : 'dark'
          }>
            Risk Level: {result.risk_level}
          </Alert>

          <RiskGauge value={result.probability * 100} />

          <div className="mt-4">
            <h6>Feature Contributions (SHAP)</h6>
            <Plot
              data={[{
                type: 'bar',
                x: result.shap_values,
                y: [
                  "Air Temp", "Process Temp", "Speed", "Torque", "Tool Wear",
                  "H", "L", "M", "Temp Diff", "Power", "Torque/Wear"
                ],
                orientation: 'h',
                marker: { color: 'rgba(0, 123, 255, 0.6)' }
              }]}
              layout={{ title: 'SHAP Feature Impact', height: 400 }}
            />
          </div>
        </div>
      )}
    </Card>
  );
};

export default PredictionForm;

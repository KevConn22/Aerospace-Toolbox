import { useState } from 'react';

export default function Atmosphere() {
  const [altitude, setAltitude] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  async function fetchData() {
    try {
      const res = await fetch('https://aero-toolbox-api.onrender.com/api/atmosphere', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ altitude: parseFloat(altitude) }),
      });

      if (!res.ok) throw new Error('Invalid input or server error.');

      const data = await res.json();
      setResult(data);
      setError('');
    } catch (err) {
      setError(err.message);
      setResult(null);
    }
  }

  return (
    <div className="p-8 max-w-lg mx-auto">
      <h1 className="text-2xl font-bold mb-4">Standard Atmosphere Calculator</h1>
      <input
        type="number"
        placeholder="Enter altitude (m)"
        value={altitude}
        onChange={(e) => setAltitude(e.target.value)}
        className="border p-2 w-full mb-4"
      />
      <button
        onClick={fetchData}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Calculate
      </button>

      {error && <p className="text-red-500 mt-4">{error}</p>}
      {result && (
        <div className="mt-6 space-y-2">
          <p><strong>Temperature:</strong> {result.temperature.toFixed(2)} K</p>
          <p><strong>Pressure:</strong> {result.pressure.toFixed(2)} Pa</p>
          <p><strong>Density:</strong> {result.density.toFixed(4)} kg/m³</p>
          <p><strong>Speed of Sound:</strong> {result.speed_of_sound.toFixed(2)} m/s</p>
        </div>
      )}
    </div>
  );
}

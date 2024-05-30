import React from 'react';
import { useParams, Navigate } from 'react-router-dom';

function ColorDetail({ colors }) {
  const { color } = useParams();
  const selectedColor = colors.find(c => c.name.toLowerCase() === color.toLowerCase());

  if (!selectedColor) return <Navigate to="/colors" />;

  return (
    <div style={{ backgroundColor: selectedColor.code, height: '100vh' }}>
      <h1>{selectedColor.name}</h1>
    </div>
  );
}

export default ColorDetail;

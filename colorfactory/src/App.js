import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Nav from './Nav';
import ColorList from './ColorList';
import ColorDetail from './ColorDetail';
import AddColorForm from './AddColorForm';

function App() {
  const initialColors = [
    { name: 'Red', code: '#FF0000' },
    { name: 'Green', code: '#00FF00' },
    { name: 'Blue', code: '#0000FF' }
  ];

  const [colors, setColors] = useState(initialColors);

  const addColor = (newColor) => {
    setColors([newColor, ...colors]);
  };

  return (
    <Router>
      <Nav />
      <Routes>
        <Route path="/colors" element={<ColorList colors={colors} />} />
        <Route path="/colors/new" element={<AddColorForm addColor={addColor} />} />
        <Route path="/colors/:color" element={<ColorDetail colors={colors} />} />
        <Route path="*" element={<Navigate to="/colors" />} />
      </Routes>
    </Router>
  );
}

export default App;

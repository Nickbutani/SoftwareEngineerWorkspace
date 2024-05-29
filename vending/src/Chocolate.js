import React from 'react';
import { Link } from 'react-router-dom';

const Chocolate = () => {
  return (
    <div>
      <h2>Chocolate</h2>
      <p>This is a delicious chocolate bar!</p>
      <Link to="/">Back to Vending Machine</Link>
    </div>
  );
};

export default Chocolate;
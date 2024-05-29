import React from 'react';
import { Link } from 'react-router-dom';

const Soda = () => {
  return (
    <div>
      <h2>Soda</h2>
      <p>This is a refreshing soda!</p>
      <Link to="/">Back to Vending Machine</Link>
    </div>
  );
};

export default Soda;
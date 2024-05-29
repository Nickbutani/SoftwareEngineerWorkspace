import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import VendingMachine from './VendingMachine';
import Chips from './Chips';
import Chocolate from './Chocolate';
import Soda from './Soda';

const App = () => {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<VendingMachine />} />
          <Route path="/chips" element={<Chips />} />
          <Route path="/chocolate" element={<Chocolate />} />
          <Route path="/soda" element={<Soda />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function AddColorForm({ addColor }) {
  const [name, setName] = useState('');
  const [code, setCode] = useState('#000000');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    addColor({ name, code });
    navigate('/colors');
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Color Name</label>
        <input
          type="text"
          id="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="code">Color Code</label>
        <input
          type="color"
          id="code"
          value={code}
          onChange={(e) => setCode(e.target.value)}
          required
        />
      </div>
      <button type="submit">Add Color</button>
    </form>
  );
}

export default AddColorForm;

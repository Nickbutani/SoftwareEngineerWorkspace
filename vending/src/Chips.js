import React, {useState} from 'react';
import { Link } from 'react-router-dom';
import './Chips.css';

const chipsImages = [
  '/images/Chazz.webp',
  '/images/Doritos.png',
  '/images/Lays.webp',
  '/images/Ruffles.png',
];

const Chips = () => {
  const [positions, setPositions] = useState([]);

  const handleClick = () => {
    const randomX = Math.floor(Math.random() * window.innerWidth);
    const randomY = Math.floor(Math.random() * window.innerHeight);
    const randomImage = chipsImages[Math.floor(Math.random() * chipsImages.length)];
    setPositions([...positions, { x: randomX, y: randomY, img: randomImage }]);
  };

  return (
    <div>
      <h2>Chips</h2>
      <p>These are some crispy chips!</p>
      <button onClick={handleClick}>Vend</button>
      <Link to="/">Back to Vending Machine</Link>
      {positions.map((pos, index) => (
        <img
          key={index}
          src={pos.img}
          alt="Chips Packet"
          style={{ 
            position: 'absolute', 
            left: `${pos.x}px`, 
            top: `${pos.y}px`, 
            width: '50px', 
            height: '50px' 
          }}
        />
      ))}
    </div>
  );
};

export default Chips;
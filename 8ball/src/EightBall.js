// EightBall.js
import React, { useState } from 'react';
import './EightBall.css';

function EightBall({ answers }) {
  const [message, setMessage] = useState("Think of a Question");
  const [color, setColor] = useState("black");

  const handleClick = () => {
    if (!answers || answers.length === 0) {
      console.error("The answers array is either undefined or empty.");
      return;
    }

    const randomAnswer = answers[Math.floor(Math.random() * answers.length)];

    if (!randomAnswer) {
      console.error("randomAnswer is undefined. Check the answers array.");
      return;
    }

    setMessage(randomAnswer.msg);
    setColor(randomAnswer.color);
  };

  return (
    <div 
      className="EightBall" 
      onClick={handleClick} 
      style={{ backgroundColor: color }}
    >
      <p>{message}</p>
    </div>
  );
}

export default EightBall;

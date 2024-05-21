import React from "react";

const Pokecard = ({ id, name, type, base_experience }) => {
    let imgSrc = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${id}.png`;
    return (
        <div className="Pokecard">
        <h1>{name}</h1>
        <img src={imgSrc} alt={name} />
        <div>Type: {type}</div>
        <div>EXP: {base_experience}</div>
        </div>
    );
}

export default Pokecard;
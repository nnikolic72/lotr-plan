import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

export const Characters = () => {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    axios.get('/api/characters/all/')
      .then((response) => {
        setCharacters(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data: ', error);
      });
  }, []);

  return (
    <div className="container">
      <h1>Characters</h1>
      <ul className="list-group">
        {characters.map((character, index) => (
          <li key={index} className="list-group-item">
            {/* Display character details here. For example: */}
            Name: {character.name}, Damage: {character.damage}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Characters;

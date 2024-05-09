import React from "react";
import "./sports.css";
import { sports } from "../data/sports_data.js";

const Sports = () => {
  return (
    <div className="container">
      <h1 className="title">2024 Summer Olympic Sports program</h1>
      <ul className="sports-list">
        {sports.map((sport) => (
          <li key={sport.id} className="sports-item">
            <div className="sport-info">
              <div className="image-container">
                <img
                  src={require(`../assets/sports_pictogram/${sport.imageId}`)}
                  alt={sport.name}
                  className="image"
                />
              </div>
              <div className="name">{sport.name}</div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sports;

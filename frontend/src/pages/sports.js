import React, { useEffect, useState } from "react";
import axios from "axios";
import "./sports.css";
import { images } from "../assets/sports_pictogram/index.js";
import mockSports from "../data/sports_data.js";

const Sports = () => {
  const [sports, setSports] = useState([]);

  const getImageFile = (imgTag) => {
    if (images[imgTag] == null) {
      return images.golf;
    }
    return images[imgTag];
  };

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/categories")
      .then((resp) => {
        let parsed = resp.data.table.map((x) => {
          if (x.id === "3x3-basketball")
            return { id: "basketball3x3", nome: "Basquete 3x3" };
          return { ...x, id: x.id.replaceAll("-", "") };
        });
        setSports(parsed);
      })
      .catch(() => setSports(mockSports));
  }, []);

  return (
    <div className="container">
      <h1 className="title">2024 Summer Olympic Sports program</h1>
      <ul className="sports-list">
        {sports.map((sport) => (
          <li key={sport.id} className="sports-item">
            <div className="sport-info">
              <div className="image-container">
                <img
                  src={getImageFile(sport.id)}
                  alt={sport.name}
                  className="image"
                />
              </div>
              <div className="name">{sport.nome}</div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sports;

import React, { useEffect, useState } from "react";
import axios from 'axios';
import { images } from '../assets/teams_flags';
import "./teams.css";
import mockTeams from "../data/teams_data.js";

const Teams = () => {
  const [teams, setTeams] = useState([]);

  const getImageFile = (imgTag) => {
    if (images[imgTag] == null) {
      return images.IOC;
    }
    return images[imgTag]
  } 

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/medals/top/20")
    .then(resp => {
      console.log(resp.data.table);
      setTeams(resp.data.table);
    }).catch(error => {
      console.log("ERROR", error);
      setTeams(mockTeams);
    })
  }, []);

  return (
    <div className="container">
      <h1 className="title">2024 Summer Olympic Top 20 National Olympic Committees</h1>
      <ul className="teams-list">
        {teams.map((team) => (
          <li key={team.id} className="teams-item">
            <div className="team-info">
              <div className="image-container">
                <img
                  src={getImageFile(team.codigo)}
                  alt={team.nome}
                  className="image"
                />
              </div>
              <div className="details">
                <div className="name">{team.nome}</div>
                <div className="athletes">Number of athletes: {team.totalAtletas}</div>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;

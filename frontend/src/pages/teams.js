import React from "react";
import "./teams.css";
import { teams } from "../data/teams_data.js";

const Teams = () => {
  return (
    <div className="container">
      <h1 className="title">2024 Summer Olympic Top 20 National Olympic Committees</h1>
      <ul className="teams-list">
        {teams.map((team) => (
          <li key={team.id} className="teams-item">
            <div className="team-info">
              <div className="image-container">
                <img
                  src={require(`../assets/teams_flags/${team.imageId}`)}
                  alt={team.name}
                  className="image"
                />
              </div>
              <div className="details">
                <div className="name">{team.name}</div>
                <div className="athletes">Number of athletes: {team.athletes}</div>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;

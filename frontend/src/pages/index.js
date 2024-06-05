import React from "react";
import './index.css'
import logo from '../assets/The Paris 2024 Summer Olympics and Paralympics.png'

const Home = () => {
  return (
    <div className="home-container">
        <img src={logo} alt="Logo" />
        <h1>Welcome to Paris 2024 Olympic HUB</h1>
      </div>
  );
};

export default Home;

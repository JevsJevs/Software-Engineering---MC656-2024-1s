import React from "react";
import './newsCards.css';

const NewsCard = ({ item, openModal }) => (
  <div className="news-card">
    <img src={require(`../../assets/news/${item.image}`)} alt={item.title} />
    <div className="news-content">
      <h2>{item.title}</h2>
      <p>{item.description}</p>
      <button onClick={() => openModal(item)} className="read-more">
        Leia mais
      </button>
    </div>
  </div>
);

export default NewsCard;

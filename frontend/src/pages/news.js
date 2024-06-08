//news.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './news.css';
import { news } from "../data/news_data.js";
import NewsCard from "../components/NewsCards/newsCards.js";
import NewsModal from "../components/NewsModal/newsModal.js";

const News = () => {
  const navigate = useNavigate();
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectedNews, setSelectedNews] = useState(null);

  const handleBack = () => {
    navigate('/');
  };

  const openModal = (newsItem) => {
    setSelectedNews(newsItem);
    setModalIsOpen(true);
  };

  const closeModal = () => {
    setModalIsOpen(false);
    setSelectedNews(null);
  };

  return (
    <div className="news-container">
      <button className="back-button" onClick={handleBack}>Voltar</button>
      <h1>Últimas Notícias</h1>
      <div className="news-feed">
        {news.map(item => (
          <NewsCard key={item.id} item={item} openModal={openModal} />
        ))}
      </div>
      {selectedNews && (
        <NewsModal
          isOpen={modalIsOpen}
          closeModal={closeModal}
          selectedNews={selectedNews}
        />
      )}
    </div>
  );
};

export default News;

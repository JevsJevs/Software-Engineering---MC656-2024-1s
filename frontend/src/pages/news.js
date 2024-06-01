import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Modal from 'react-modal';
import './news.css';
import { news } from "../data/news_data.js";

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
          <div key={item.id} className="news-card">
            <img src={item.image} alt={item.title} />
            <div className="news-content">
              <h2>{item.title}</h2>
              <p>{item.description}</p>
              <button onClick={() => openModal(item)} className="read-more">Leia mais</button>
            </div>
          </div>
        ))}
      </div>
      {selectedNews && (
        <Modal
          isOpen={modalIsOpen}
          onRequestClose={closeModal}
          contentLabel="News Modal"
          className="news-modal"
          overlayClassName="news-overlay"
        >
          <h2>{selectedNews.title}</h2>
          <img src={selectedNews.image} alt={selectedNews.title} />
          <p>{selectedNews.content}</p>
          <button onClick={closeModal} className="close-modal-button">Fechar</button>
        </Modal>
      )}
    </div>
  );
};

export default News;

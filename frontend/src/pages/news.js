import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './news.css';
import { news as initialNews } from "../data/news_data.js";
import NewsCard from "../components/NewsCards/newsCards.js";
import NewsModal from "../components/NewsModal/newsModal.js";
import CreateNewsModal from "../components/createNewsModal/createNewsModal.js";

const News = () => {
  const navigate = useNavigate();
  const [news, setNews] = useState(initialNews);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [createModalIsOpen, setCreateModalIsOpen] = useState(false);
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

  const openCreateModal = () => {
    setCreateModalIsOpen(true);
  };

  const closeCreateModal = () => {
    setCreateModalIsOpen(false);
  };

  const addNews = (newNews) => {
    setNews([newNews, ...news]);
  };

  return (
    <div className="news-container">
      <button className="back-button" onClick={handleBack}>Voltar</button>
      <button className="create-news-button" onClick={openCreateModal}>Criar Notícia</button>
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
      <CreateNewsModal
        isOpen={createModalIsOpen}
        closeModal={closeCreateModal}
        addNews={addNews}
      />
    </div>
  );
};

export default News;

import React from 'react';
import Modal from 'react-modal';
import '../NewsModal/newsModal.css';

const NewsModal = ({ isOpen, closeModal, selectedNews }) => (
  <Modal
    isOpen={isOpen}
    onRequestClose={closeModal}
    contentLabel="News Modal"
    className="news-modal"
    overlayClassName="news-overlay"
  >
    <h2>{selectedNews.title}</h2>
    <img src={require(`../../assets/news/${selectedNews.image}`)} alt={selectedNews.title} />
    <p>{selectedNews.content}</p>
    <button onClick={closeModal} className="close-modal-button">Fechar</button>
  </Modal>
);

export default NewsModal;

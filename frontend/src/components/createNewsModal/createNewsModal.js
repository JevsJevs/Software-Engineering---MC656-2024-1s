import React, { useState } from 'react';
import Modal from 'react-modal';
import './createNewsModal.css';

const CreateNewsModal = ({ isOpen, closeModal, addNews }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [content, setContent] = useState('');
  // eslint-disable-next-line
  const [image, setImage] = useState(null);
  const [imageUrl, setImageUrl] = useState(null);

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    setImage(file);
    setImageUrl(URL.createObjectURL(file));
  };

  const handleSubmit = (e) => {
    e.preventDefault(); // Evita o comportamento padrão do submit
    closeModal(); // Fecha o modal
  };

  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={closeModal}
      contentLabel="Create News Modal"
      className="news-modal"
      overlayClassName="news-overlay"
    >
      <h2>Create New News</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Title"
          maxLength="50"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Description"
          maxLength="100"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <textarea
          placeholder="Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
        ></textarea>
        <input type="file" onChange={handleImageUpload} required />
        {imageUrl && <img src={imageUrl} alt="Preview" style={{ width: '100px', height: '100px', marginTop: '10px' }} />}
        <button type="submit">Save</button>
      </form>
      <button onClick={closeModal} className="close-modal-button">Close</button>
    </Modal>
  );
};

export default CreateNewsModal;

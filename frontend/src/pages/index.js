import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import "./index.css";
import { news } from "../data/news_data.js";
import { events } from "../data/events_data.js";
import { facts as mock_facts } from "../data/facts_data.js";
import { watchLocations } from "../data/watch_data.js";
import { sponsors } from "../data/sponsors_data.js";

const Home = () => {
  const navigate = useNavigate();
  const [currentNewsIndex, setCurrentNewsIndex] = useState(0);
  const [facts, setFacts] = useState(mock_facts)

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentNewsIndex((prevIndex) => (prevIndex + 1) % news.length);
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  const handlePrevNews = () => {
    setCurrentNewsIndex(
      (prevIndex) => (prevIndex - 1 + news.length) % news.length
    );
  };

  const handleNextNews = () => {
    setCurrentNewsIndex((prevIndex) => (prevIndex + 1) % news.length);
  };

  const handleViewAllNews = () => {
    navigate("/news");
  };

  useEffect(() => {
    // Atualizar o fato com o país com mais medalhas de ouro
    axios.get("http://127.0.0.1:5000/medals/top/1")
      .then(resp => {
        const country = resp.data.table[0].nome;
        const newFacts = facts.map(f => {
          if (f.id === 1) {
            return {
              ...f,
              fact: `País com mais medalhas de ouro: ${country}`
            };
          }
          return f;
        });
        setFacts(newFacts);
      })
      .catch(error => {
        console.error('Erro ao fazer a solicitação Axios:', error);
      });

    // Atualizar o fato com o número de países participantes
    axios.get("http://127.0.0.1:5000/medals/")
      .then(resp => {
        const newFacts = facts.map(f => {
          if (f.id === 2) {
            return {
              ...f,
              fact: `${resp.data.table.length} países participam das Olimpíadas`
            };
          }
          return f;
        });
        setFacts(newFacts);
      })
      .catch(error => {
        console.error('Erro ao fazer a solicitação Axios:', error);
      });
    // eslint-disable-next-line
  }, []);

  return (
    <div className="home-container">
      <section className="banner">
        <div className="news-carousel">
          <button className="carousel-control prev" onClick={handlePrevNews}>
            &lt;
          </button>
          {news.map((item, index) => (
            <div
              key={item.id}
              className={`news-item ${index === currentNewsIndex ? "active" : ""}`}
            >
              <img
                src={require(`../assets/news/${item.image}`)}
                alt={item.title}
              />
              <h2>{item.title}</h2>
            </div>
          ))}
          <button className="carousel-control next" onClick={handleNextNews}>
            &gt;
          </button>
        </div>
        <button className="all-news-button" onClick={handleViewAllNews}>
          Ver todas as notícias
        </button>
      </section>

      <section className="events">
        <h2>Próximos Eventos</h2>
        <div className="event-cards">
          {events.map((event) => (
            <div key={event.id} className="event-card">
              <h3>{event.sport}</h3>
              <p>
                {event.date} às {event.time}
              </p>
            </div>
          ))}
        </div>
      </section>

      <section className="facts">
        <h2>Curiosidades</h2>
        <div className="fact-cards">
          {facts.map((fact) => (
            <div key={fact.id} className="fact-card">
              <p>{fact.fact}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="watch-locations">
        <h2>Onde Assistir</h2>
        <div className="location-cards">
          {watchLocations.map((location) => (
            <div key={location.id} className="location-card">
              <a href={location.link} target="_blank" rel="noopener noreferrer">
                <img src={require(`../assets/watch/${location.logo}`)} alt={location.name} />
              </a>
            </div>
          ))}
        </div>
      </section>

      <section className="sponsors">
        <h2>Patrocinadores</h2>
        <div className="sponsor-cards">
          {sponsors.map((sponsor) => (
            <div key={sponsor.id} className="sponsor-card">
              <a href={sponsor.link} target="_blank" rel="noopener noreferrer">
                <img src={require(`../assets/sponsors/${sponsor.logo}`)} alt={sponsor.name} />
              </a>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default Home;

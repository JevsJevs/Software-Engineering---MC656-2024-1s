import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./index.css";
import { news } from "../data/news_data.js";
import { events } from "../data/events_data.js";
import { facts } from "../data/facts_data.js";
import { watchLocations } from "../data/watch_data.js";
import { sponsors } from "../data/sponsors_data.js";

const Home = () => {
  const navigate = useNavigate();
  const [currentNewsIndex, setCurrentNewsIndex] = useState(0);

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
              className={`news-item ${
                index === currentNewsIndex ? "active" : ""
              }`}
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

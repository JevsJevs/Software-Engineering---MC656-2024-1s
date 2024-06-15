import React from "react";
import "./about.css";
import logo from "../assets/logo_olimpix.webp";

const About = () => {
  return (
    <div className="about-container">
      <div className="text-section">
        <h1>About Us</h1>
        <div className="text-content">
          <p>
            Welcome to OlimpiX, where innovation meets passion for sports and
            technology. We are a dedicated team of developers, designers, and
            enthusiasts committed to crafting exceptional digital experiences for
            the upcoming Paris 2024 Summer Olympics. At OlimpiX, we believe
            in the power of technology to connect, engage, and inspire, and we're
            thrilled to be at the forefront of the digital transformation
            surrounding this global event.
          </p>
          <p>
            Our journey began with a shared vision: to create a centralized hub that
            celebrates the spirit of the Olympics while leveraging the latest
            advancements in application development. With Paris 2024 on the horizon,
            we saw an opportunity to redefine how fans, athletes, and organizers
            experience the games. Thus, our mission was born: to build a
            comprehensive platform that brings the magic of the Olympics to life in
            the digital realm.
          </p>
          <p>
            What sets us apart is our relentless commitment to excellence. From
            intuitive user interfaces to cutting-edge features, every aspect of our
            applications is meticulously designed and developed to deliver an
            unparalleled user experience. Whether you're a sports enthusiast
            following your favorite athletes, a traveler planning your Olympic
            journey, or a local looking to engage with the excitement right at your
            doorstep, OlimpiX has you covered.
          </p>
          <p>
            But our dedication doesn't stop there. As advocates for inclusivity and
            accessibility, we strive to ensure that our platform is accessible to
            everyone, regardless of ability or background. Through thoughtful design
            and inclusive features, we aim to create a space where every individual
            can share in the Olympic spirit and feel like an integral part of the
            experience.
          </p>
          <p>
            At OlimpiX, we're more than just a technology company — we're a
            community. We're driven by a shared passion for sports, technology, and
            the transformative power of human connection. As we embark on this
            exhilarating journey towards Paris 2024, we invite you to join us in
            shaping the future of Olympic engagement. Together, let's celebrate the
            thrill of competition, the beauty of diversity, and the boundless
            potential of innovation.
          </p>
          <p className="last-paragraph">
            Join us at OlimpiX, and let's make history together.
          </p>
        </div>
      </div>
      <div className="image-section">
        <img src={logo} alt="OlimpiX" />
      </div>
    </div>
  );
};

export default About;

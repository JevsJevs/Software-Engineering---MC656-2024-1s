// components/Navbar/index.js

import React from "react";
import { Nav, NavLink, Bars, NavMenu } from "./NavbarElements.js";
import logo from "../../assets/The Paris 2024 Summer Olympics and Paralympics.png";

const Navbar = () => {
  return (
    <>
      <Nav>
      <img src={logo} alt="Logo" style={{ height: '85px'}} /> 
        <Bars />
        <NavMenu>
          <NavLink to="/" activeStlye>
            Home
          </NavLink>
          <NavLink to="/table" activeStyle>
            Table
          </NavLink>
          <NavLink to="/sports" activeStyle>
            Sports
          </NavLink>
          <NavLink to="/teams" activeStyle>
            Teams
          </NavLink>
          <NavLink to="/about" activeStlye>
            About Us
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};

export default Navbar;

// components/Navbar/index.js

import React from "react";
import { Nav, NavLink, Bars, NavMenu } from "./NavbarElements.js";
import logo from "../../assets/Paris2024_OlyEmbleme_RVB_Mono_Noir_2021.png.png";
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

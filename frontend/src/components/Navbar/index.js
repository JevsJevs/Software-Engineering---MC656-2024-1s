// components/Navbar/index.js

import React from "react";
import { Nav, NavLink, Bars, NavMenu } from "./NavbarElements.js";

const Navbar = () => {
  return (
    <>
      <Nav>
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

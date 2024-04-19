// pages/events.js

import React from "react";
import './table.css'
import logo from '../assets/The Paris 2024 Summer Olympics and Paralympics.png'

const Table = () => {
  return (
      <div className="table-container">
        <img src={logo} alt="Logo" />
        <h1>Paris 2024 Olympic Medal Table</h1>
        <table>
          <thead>
            <tr>
              <th>Team</th>
              <th>Gold</th>
              <th>Silver</th>
              <th>Bronze</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Brazil</td>
              <td>10</td>
              <td>3</td>
              <td>2</td>
              <td>15</td>
            </tr>
            <tr>
              <td>France</td>
              <td>5</td>
              <td>2</td>
              <td>1</td>
              <td>8</td>
            </tr>
            <tr>
              <td>Japan</td>
              <td>3</td>
              <td>1</td>
              <td>0</td>
              <td>4</td>
            </tr>
          </tbody>
        </table>
      </div>
  );
};

export default Table;

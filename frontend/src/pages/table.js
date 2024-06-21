import { React, useState, useEffect } from "react";
import "./table.css";
import logo from "../assets/The Paris 2024 Summer Olympics and Paralympics.png";

const Table = () => {
  const [tableRows, setTableRows] = useState([]);
  const [values, setValues] = useState([]);
  
  const parseCSV = (str) => {
    const rows = str.split('\n').filter(Boolean);
    const header = rows[0].split(',');
    const values = rows.slice(1).map(row => row.split(','));
  
    return { header, values };
  };
  useEffect(() => {
    fetch("./Olympics_Medal_Table.csv")
      .then((response) => response.text())
      .then((csv) => {
        const { header, values } = parseCSV(csv);

        setTableRows(header);
        setValues(values);
      })
      .catch((error) => console.error("Error fetching CSV file:", error));
  }, []);

  return (
    <div className="table-container">
      <img src={logo} alt="Logo" />
      <h1>Paris 2024 Olympic Medal Table</h1>
      <table>
        <thead>
          <tr>
            {tableRows.map((row, index) => (
              <th key={index}>{row}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {values.map((row, index) => (
            <tr key={index}>
              {row.map((val, i) => (
                <td key={i}>{val}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;

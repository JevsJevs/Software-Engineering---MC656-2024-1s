import { React, useState, useEffect } from "react";
import "./table.css";
import logo from "../assets/The Paris 2024 Summer Olympics and Paralympics.png";
import Papa from "papaparse";

const Table = () => {
  // eslint-disable-next-line no-unused-vars
  const [parsedData, setParsedData] = useState([]);
  const [tableRows, setTableRows] = useState([]);
  const [values, setValues] = useState([]);

  useEffect(() => {
    fetch("./Olympics_Medal_Table.csv")
      .then((response) => response.text())
      .then((csv) => {
        Papa.parse(csv, {
          header: true,
          skipEmptyLines: true,
          complete: function (results) {
            const rowsArray = [];
            const valuesArray = [];

            results.data.forEach((d) => {
              rowsArray.push(Object.keys(d));
              valuesArray.push(Object.values(d));
            });

            setParsedData(results.data);
            setTableRows(rowsArray[0]);
            setValues(valuesArray);
          },
        });
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

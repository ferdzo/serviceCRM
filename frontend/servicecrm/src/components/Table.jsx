import Row from "./Row";
import React, { useEffect, useState } from "react";
import axios from "axios";
import Search from "./Search";

export default function Table() {
  const [data, setData] = useState([]);
  const [filteredData, setFilteredData] = useState([]);
  const [searchValue, setSearchValue] = useState("");

  useEffect(() => {
    axios.get("http://localhost:8000/api/").then((response) => {
      setData(response.data);
    });
  }, []);

  useEffect(() => {
    if (searchValue){
      debugger;
      for (const item in data) {
        if (item.name.toLowerCase().includes(searchValue.toLowerCase())){
          setFilteredData((prev) => {
            return [...prev, item];
          });
        }
      }
  }
  }, [searchValue, data]);

  const Done = data?.inserts?.filter((item) => item.done === true);
  const NotDone = data?.inserts?.filter((item) => item.done === false);
  var isDone = true;

  const handleValue = (value) => {
    setSearchValue(value);
  };

  return (
    <div>
      <Search data={data} handleValue={handleValue} />

      <table className="table"></table>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Name</th>
            <th scope="col">Date</th>
            <th scope="col">Phone</th>
            <th scope="col">Description</th>
            <th scope="col">Repair</th>
            <th scope="col">Plateno</th>
            <th scope="col">Note</th>
            <th scope="col">Done</th>
          </tr>
        </thead>
        <tbody>
          {filteredData.map((item) => {
            return <Row key={item.id} item={item} />;
          })}
        </tbody>
      </table>
    </div>
  );
}

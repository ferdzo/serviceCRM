import Row from "./Row";
import React, { useEffect, useState } from "react";
import axios from 'axios';

export default function Table() {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/').then(
            (response) => {
                setData(response.data);
            });
    }, []);
    console.log(data);
    const Done = data && data.inserts && data.inserts.filter((item) => item.done === true);
    const NotDone = data && data.inserts && data.inserts.filter((item) => item.done === false);
    var isDone = true;
    return (
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
                { isDone 
                    ? NotDone && NotDone.map((item) => <Row key={item.id} item={item} />)
                    : Done && Done.map((item) =>  <Row key={item.id} item={item} />)
                }
            </tbody>
        </table>
    );
}
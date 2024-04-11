import React from 'react';

function TableRow({ item }) {
        const isDone = item.done? "✅":"❌";
    return (
        <tr>
            <th scope="row">{item.id}</th>
            <td>{item.name}</td>
            <td>{item.date}</td>
            <td>{item.phone}</td>
            <td>{item.description}</td>
            <td>{item.repair}</td>
            <td>{item.plateno}</td>
            <td>{item.note}</td>
            <td>{isDone}</td>
        </tr>
    );
}

export default TableRow;
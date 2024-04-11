import React from 'react';
import {useState} from 'react';

function MyButton(){
    const [count, setCount]=useState(0);
  
    function handleClick(){
      setCount(count+1);
    }

    return(
        <div>
            <Dugme count={count} handleClick={handleClick}/>
            <Dugme count={count} handleClick={handleClick}/>
        </div>
        

    )
}

function Dugme({count, handleClick}){
    return(
        <button onClick={handleClick}>Clicked {count} times</button>
    )
}
export default MyButton;
import React from 'react';
import logo from './logo.svg';
import './App.css';
import teacher_data from './teachers.json';


function App() {
  return (
    <div className="App">
      { teacher_data?.result.map(({ name }) => (
        <div>{name}</div>
      )) }
    </div>
  );
}

export default App;

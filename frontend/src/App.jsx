import React from 'react';
import CalcDistanceForm from './components/distanceForm';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <div className="content-wrapper">
        <CalcDistanceForm />
      </div>
      <footer className="app-footer">
        Made with ❤️ by Nandan Kakadiya
      </footer>
    </div>
  );
};

export default App;
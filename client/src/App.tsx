// src/App.tsx
import React from 'react';
import Navbar from './components/LayoutArea/Layout/Navbar';
import Routes from './components/RoutingArea/Routes';
import './App.css';

const App: React.FC = () => {
    return (
      <div className="App">
        <Navbar />
        <Routes />
      </div>
    );
  }
  
  export default App;
// src/App.tsx
import React from 'react';
import Navbar from './components/LayoutArea/Layout/Navbar';
import Routes from './components/RoutingArea/Routes';
import './App.css';
import 'ui-neumorphism/dist/index.css';

const App: React.FC = () => {
    return (
      <div className="App">
        <Navbar />
        <Routes /> {/* Ensure that Routes does NOT contain a BrowserRouter */}
      </div>
    );
};

export default App;

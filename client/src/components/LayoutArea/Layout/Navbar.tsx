// src/components/LayoutArea/Navbar.tsx
import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Import the CSS file

const Navbar: React.FC = () => (
  <nav className="navbar">
    <div className="navbar-container">
      <div className="navbar-logo">
        <Link to="/">MyApp</Link>
      </div>
      <ul className="navbar-menu">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/statistics">Statistics</Link></li>
        <li><Link to="/about">About</Link></li>
      </ul>
    </div>
    <div className="divider" />
  </nav>
);

export default Navbar;

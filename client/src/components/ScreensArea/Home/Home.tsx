import React from 'react';
import '../../../components/ScreensArea/Home/Home.css';

const Home: React.FC = () => (
  <div className="home-container">
    <div className="neumorphic-card">
      <h1 style={{ margin: 0 }}>Welcome to the Vacation Management System</h1>
      <p>This system provides statistics about vacations.</p>
      <img src="/path/to/your/image.jpg" alt="Statistics" style={{ width: '100%', height: 'auto' }} />
    </div>
  </div>
);

export default Home;

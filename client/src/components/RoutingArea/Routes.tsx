// src/components/RoutingArea/Routes.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from '../ScreensArea/Home/Home';
import Login from '../AuthArea/Login/Login';
import Statistics from '../ScreensArea/Statistics/Statistics';
import About from '../ScreensArea/About/About';
import NotFound from '../ScreensArea/NotFound';

const AppRoutes: React.FC = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/statistics" element={<Statistics />} />
      <Route path="/about" element={<About />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  </Router>
);

export default AppRoutes;
// src/components/RoutingArea/Routes.tsx

import React from 'react';
import { Route, Routes } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { RootState } from '../../reducers';
import Home from '../ScreensArea/Home/Home';
import Login from '../AuthArea/Login/Login';
import Statistics from '../ScreensArea/Statistics/Statistics';
import About from '../ScreensArea/About/About';
import NotFound from '../ScreensArea/NotFound';

const AppRoutes: React.FC = () => {
  const user = useSelector((state: RootState) => state.user);

  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/about" element={<About />} />
      {user ? (
        <>
          <Route path="/statistics" element={<Statistics />} />
          {/* Add other protected routes here */}
        </>
      ) : (
        <Route path="/login" element={<Login />} />
      )}
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
};

export default AppRoutes;
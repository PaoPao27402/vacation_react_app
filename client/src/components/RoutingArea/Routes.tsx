import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from '../ScreensArea/Home/Home';
import Login from '../components/AuthArea/Login/Login';
import Statistics from '../ScreensArea/Statistics/Statistics';
import About from '../ScreensArea/About/About';
import NotFound from '../ScreensArea/NotFound';

const Routes: React.FC = () => (
  <Router>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route path="/login" component={Login} />
      <Route path="/statistics" component={Statistics} />
      <Route path="/about" component={About} />
      <Route component={NotFound} />
    </Switch>
  </Router>
);

export default Routes;
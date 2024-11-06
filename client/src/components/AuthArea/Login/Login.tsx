import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import authService from '../../../service/authService';
import '../../../components/AuthArea/Login/Login.css';
import CustomCardContent from './CustomCardContent';

const Login: React.FC = () => {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!email || !password) {
      console.error('Email and password are required');
      return;
    }
    try {
      await authService.login(email, password);
      navigate('/statistics');
    } catch (error) {
      console.error('Login failed', error);
    }
  };

  return (
    <div className="login-container">
      <div className="custom-card">
        <CustomCardContent className="neumorphic-card">
          <h1>Login</h1>
          <form onSubmit={handleLogin}>
            <div style={{ marginBottom: '20px' }}>
              <input
                className="text-field"
                placeholder="Email"
                type="email"
                value={email}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}
              />
            </div>
            <div style={{ marginBottom: '20px' }}>
              <input
                className="text-field"
                placeholder="Password"
                type="password"
                value={password}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}
              />
            </div>
            <div className="card-action">
              <button type="submit" className="button">Login</button>
            </div>
          </form>
        </CustomCardContent>
      </div>
    </div>
  );
};

export default Login;

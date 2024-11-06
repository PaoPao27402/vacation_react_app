// src\service\authService.tsx

import axios from 'axios';
import { jwtDecode } from "jwt-decode";
import store from '../store';
import { userLoggedIn, userLogout } from '../reducers/userAction';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

interface LoginResponse {
  access: string;
  refresh: string;
}

const login = async (email: string, password: string): Promise<void> => {
  try {
    const response = await axios.post<LoginResponse>(`${API_URL}/token/`, { email, password });
    const { access, refresh } = response.data;

    // Decode the token to get user information
    const decoded: any = jwtDecode(access);
    const user = {
      email: decoded.email,
      password: '', // You might not want to store the password here
      is_superuser: decoded.is_superuser,
      first_name: decoded.first_name,
      last_name: decoded.last_name,
    };

    store.dispatch(userLoggedIn(user));

    localStorage.setItem('accessToken', access);
    localStorage.setItem('refreshToken', refresh);
  } catch (error) {
    console.error("Login error:", error);
    throw new Error('Login failed');
  }
};

const logout = async (): Promise<void> => {
  try {
    await axios.post(`${API_URL}/logout/`, {}, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
      },
    });
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    store.dispatch(userLogout());
  } catch (error) {
    console.error("Logout error:", error);
    throw new Error('Logout failed');
  }
};

const getAccessToken = (): string | null => {
  return localStorage.getItem('accessToken');
};

const authService = {
  login,
  logout,
  getAccessToken,
};

export default authService;
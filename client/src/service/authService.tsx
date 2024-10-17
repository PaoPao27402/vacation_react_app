import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

interface LoginResponse {
  access: string;
  refresh: string;
}

const login = async (email: string, password: string): Promise<void> => {
  try {
    const response = await axios.post<LoginResponse>(`${API_URL}/login/`, { email, password });
    const { access, refresh } = response.data;
    localStorage.setItem('accessToken', access);
    localStorage.setItem('refreshToken', refresh);
  } catch (error) {
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
  } catch (error) {
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
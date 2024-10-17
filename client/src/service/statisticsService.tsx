// src/service/statisticsService.tsx
import axios from 'axios';
import authService from './authService';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

interface Statistics {
  past_vacations: number;
  on_going_vacations: number;
  future_vacations: number;
  total_users: number;
  total_likes: number;
  likes_distribution: { destination: string; likes: number }[];
}

const getStatistics = async (): Promise<Statistics> => {
  try {
    const response = await axios.get<Statistics>(`${API_URL}/statistics/`, {
      headers: {
        Authorization: `Bearer ${authService.getAccessToken()}`,
      },
    });
    return response.data;
  } catch (error) {
    throw new Error('Failed to fetch statistics');
  }
};

const getUserCount = async (): Promise<number> => {
  try {
    const response = await axios.get<{ total_users: number }>(`${API_URL}/user-count/`, {
      headers: {
        Authorization: `Bearer ${authService.getAccessToken()}`,
      },
    });
    return response.data.total_users;
  } catch (error) {
    throw new Error('Failed to fetch user count');
  }
};

const getLikesCount = async (): Promise<number> => {
  try {
    const response = await axios.get<{ total_likes: number }>(`${API_URL}/likes-count/`, {
      headers: {
        Authorization: `Bearer ${authService.getAccessToken()}`,
      },
    });
    return response.data.total_likes;
  } catch (error) {
    throw new Error('Failed to fetch likes count');
  }
};

const getLikesDistribution = async (): Promise<{ destination: string; likes: number }[]> => {
  try {
    const response = await axios.get<{ destination: string; likes: number }[]>(`${API_URL}/likes-distribution/`, {
      headers: {
        Authorization: `Bearer ${authService.getAccessToken()}`,
      },
    });
    return response.data;
  } catch (error) {
    throw new Error('Failed to fetch likes distribution');
  }
};

const statisticsService = {
  getStatistics,
  getUserCount,
  getLikesCount,
  getLikesDistribution,
};

export default statisticsService;
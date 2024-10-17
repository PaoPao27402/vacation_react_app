// src/components/ScreensArea/Statistics.tsx
import React, { useEffect, useState } from 'react';
import statisticsService from '../../service/statisticsService';

interface Statistics {
  past_vacations: number;
  on_going_vacations: number;
  future_vacations: number;
  total_users: number;
  total_likes: number;
  likes_distribution: { destination: string; likes: number }[];
}

const Statistics: React.FC = () => {
  const [statistics, setStatistics] = useState<Statistics | null>(null);

  useEffect(() => {
    const fetchStatistics = async () => {
      try {
        const data = await statisticsService.getStatistics();
        setStatistics(data);
      } catch (error) {
        console.error('Failed to fetch statistics', error);
      }
    };

    fetchStatistics();
  }, []);

  if (!statistics) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Statistics</h1>
      <p>Past</p>
    </div>
  )
 
// src/components/ScreensArea/Statistics/Statistics.tsx
import React, { useEffect, useState } from 'react';
import statisticsService from '../../../../src/service/statisticsService';

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
      <p>Past Vacations: {statistics.past_vacations}</p>
      <p>Ongoing Vacations: {statistics.on_going_vacations}</p>
      <p>Future Vacations: {statistics.future_vacations}</p>
      <p>Total Users: {statistics.total_users}</p>
      <p>Total Likes: {statistics.total_likes}</p>
      <h2>Likes Distribution</h2>
      <ul>
        {statistics.likes_distribution.map((item) => (
          <li key={item.destination}>
            {item.destination}: {item.likes} likes
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Statistics;
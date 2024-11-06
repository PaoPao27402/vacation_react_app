// Likes.tsx
import React from 'react';
import CustomCircularChart from '../CustomCharts/CustomCircularChart'; 

const countryChartData = [
  { id: '1', value: 20, label: 'Country A', color: 'var(--primary)' },
  { id: '2', value: 40, label: 'Country B', color: 'var(--info)' },
  { id: '3', value: 60, label: 'Country C', color: 'var(--warning)' },
  { id: '4', value: 80, label: 'Country D', color: 'var(--success)' },
  { id: '5', value: 100, label: 'Country E', color: 'var(--error)' },
];

const vacationChartData = [
  { id: '1', value: 30, label: 'Vacation A', color: 'var(--primary)' },
  { id: '2', value: 50, label: 'Vacation B', color: 'var(--info)' },
  { id: '3', value: 70, label: 'Vacation C', color: 'var(--warning)' },
];

const Likes: React.FC = () => {
  return (
    <div>
      <CustomCircularChart data={countryChartData} title="Likes by Country" />
      <CustomCircularChart data={vacationChartData} title="Likes by Vacation" />
    </div>
  );
};

export default Likes;

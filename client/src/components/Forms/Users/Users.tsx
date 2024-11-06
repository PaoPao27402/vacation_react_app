// Users.tsx
import React from 'react';
import CustomCircularChart from '../CustomCharts/CustomCircularChart'; 

const userData = [
  { id: '1', value: 30, label: 'User Group A', color: 'var(--primary)' },
  { id: '2', value: 50, label: 'User Group B', color: 'var(--info)' },
  { id: '3', value: 70, label: 'User Group C', color: 'var(--warning)' },
];

const Users: React.FC = () => {
  return (
    <div>
      <CustomCircularChart data={userData} title="Users by Category" />
    </div>
  );
};

export default Users;

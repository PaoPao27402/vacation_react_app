// CustomCircularChart.tsx
import React from 'react';
import { ProgressCircular } from 'ui-neumorphism';

interface CircularChartItem {
  id: string | number;
  value: number; // Percentage value from 0 to 100
  label: string;
  color: string; // CSS color value
}

interface CustomCircularChartProps {
  data: CircularChartItem[];
  title: string;
}

const CustomCircularChart: React.FC<CustomCircularChartProps> = ({ data, title }) => {
  return (
    <div
      style={{
        width: '100%',
        padding: '16px',
        borderRadius: '8px', // Mimicking the Card style
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.1)', // Mimicking the neumorphism style
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <h2 style={{ textAlign: 'center', margin: '0' }}>{title}</h2>
      <div style={{ display: 'flex', justifyContent: 'space-around', width: '100%' }}>
        {data.map((item) => (
          <div key={item.id} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <ProgressCircular elevated value={item.value} size={64} width={8} color={item.color} />
            <span style={{ marginTop: '8px' }}>{item.label}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CustomCircularChart;

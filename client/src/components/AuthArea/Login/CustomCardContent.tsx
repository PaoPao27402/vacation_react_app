import React from 'react';

interface CustomCardContentProps {
  children: React.ReactNode;
  className?: string;
}

const CustomCardContent: React.FC<CustomCardContentProps> = ({ children, className }) => {
  return <div className={className}>{children}</div>;
};

export default CustomCardContent;

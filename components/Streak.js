import React from 'react';

const Streak = ({ count }) => {
  return (
    <div className="streak">
      <p>Current Streak: {count}</p>
    </div>
  );
};

export default Streak;

import React from 'react';
import { render, screen } from '@testing-library/react';
import Streak from './Streak';

test('renders streak count', () => {
  render(<Streak count={5} />);
  const streakElement = screen.getByText(/Current Streak: 5/i);
  expect(streakElement).toBeInTheDocument();
});

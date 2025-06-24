import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';
import * as api from './api';

test('renders chat header', () => {
  render(<App />);
  const header = screen.getByText(/Dune GM Chat UI/i);
  expect(header).toBeInTheDocument();
});

test('roll button fetches dice', async () => {
  jest.spyOn(api, 'fetchD20').mockResolvedValue(5);
  render(<App />);
  fireEvent.click(screen.getByText(/Roll 1d20/i));
  await waitFor(() => screen.getByText(/You rolled a 5/i));
});

test('roll 2d20 button fetches dice array', async () => {
  jest.spyOn(api, 'fetch2D20').mockResolvedValue([3, 17]);
  render(<App />);
  fireEvent.click(screen.getByText(/Roll 2d20/i));
  await waitFor(() => screen.getByText(/You rolled 3 and 17/i));
});

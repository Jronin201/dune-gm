import { render, screen } from '@testing-library/react';
import App from './App';

test('renders chat header', () => {
  render(<App />);
  const header = screen.getByText(/Dune GM Chat UI/i);
  expect(header).toBeInTheDocument();
});

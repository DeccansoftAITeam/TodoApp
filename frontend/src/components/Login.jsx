import { useState } from 'react';
import axios from 'axios';

function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const resp = await axios.post(localStorage.getItem("URL") + '/api/auth/login', { username, password });
      const token = resp.data?.access_token;
      if (token) {
        localStorage.setItem('token', token);
        setError('');
        onLogin();
      }
    } catch (err) {
      setError('Invalid credentials');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form onSubmit={handleSubmit} className="w-full max-w-md bg-white p-6 rounded shadow">
        <h2 className="text-2xl font-bold mb-4">Login</h2>
        {error && <div className="text-red-600 mb-2">{error}</div>}
        <div className="mb-4">
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full px-4 py-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full px-4 py-2 border rounded"
          />
        </div>
        <button className="w-full bg-blue-500 text-white py-2 rounded">Login</button>
      </form>
    </div>
  );
}

export default Login;

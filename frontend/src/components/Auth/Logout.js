import React, { useState } from 'react';
import './Auth.css';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = async event => {
    event.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/api/getJwtToken', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
      });

      if (!response.ok) {
        throw new Error('Ошибка входа');
      }

      const data = await response.json();

      localStorage.setItem('token', data.token);

      window.location.href = '/';
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <div className="auth-container">
      <h2>Вход</h2>
      {error && <p>{error}</p>}
      <form onSubmit={handleSubmit} className="auth-form">
        <label>
          Имя пользователя:
          <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
        </label>
        <label>
          Пароль:
          <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
        </label>
        <input type="submit" value="Войти" />
      </form>
    </div>
  );
}

export default Login;

import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { Link } from 'react-router-dom';

import './Auth.css';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async event => {
    event.preventDefault();
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/login', {
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
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className='auth-container'>
      <h>
        Войти в аккаунт
      </h>
      <Form>
        {error && <p>{error}</p>}
        <Form.Group className='mb-3'>
          <Form.Label>Логин</Form.Label>
          <Form.Control type='text' value={username} onChange={e => setUsername(e.target.value)} />
          <Form.Text className='text-muted'>
            Введите имя пользователя
          </Form.Text>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Пароль</Form.Label>
          <Form.Control type="password" value={password} onChange={e => setPassword(e.target.value)} />
        </Form.Group>

        <Button variant="primary" onSubmit={handleSubmit} disabled={isLoading}>
          Войти
        </Button>
      </Form>
      <h>Нет аккаунта? <Link to='/register'>зарегистрироваться</Link></h>
    </div>
  );
}

export default Login;

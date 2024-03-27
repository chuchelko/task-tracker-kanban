import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { Link, Navigate } from 'react-router-dom';

import './Auth.css';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({username: '', password: ''});
  const [isFormValid, setIsFormValid] = useState(false);

  useEffect(() => {
    setIsFormValid(username.trim() !== '' && password.trim() !== '');
  }, [username, password]);

  const validateForm = () => {
    let newErrors = {username: '', password: ''};
    let formIsValid = true;

    if(username.trim() === '') {
      newErrors.username = 'Введите имя пользователя';
      formIsValid = false;
    }

    if(password.trim() === '') {
      newErrors.password = 'Введите пароль';
      formIsValid = false;
    }

    setErrors(newErrors);
    return formIsValid;
  };

  const handleSubmit = async event => {
    event.preventDefault();
    setErrors({username: '', password: ''})
    if(!validateForm()) {
      return;
    }

    try {
      const name = username;
      const response = await fetch('http://localhost:8000/api/user/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, password })
      });

      if (!response.ok) {
        throw new Error(response.error);
      }

      const data = await response.json();
      localStorage.setItem('accessToken', data.access_token);
      localStorage.setItem('refresh_token', data.refresh_token);
      window.location.href = '/';
    } catch (error) {
      setErrors({username: 'Имя пользователя и/или пароль введены некорректно', password: ' '});
    }
  };

  if(localStorage.getItem('accessToken') != null) {
    return <Navigate to='/'/>
  }

  return (
    <div className='auth-container'>
      <Form>
        <Form.Group className='mb-3' controlId="formBasicUsername" isInvalid={!!errors.username}>
          <Form.Label>Логин</Form.Label>
          <Form.Control type='text' value={username} onChange={e => setUsername(e.target.value)} isInvalid={!!errors.username} />
          <Form.Control.Feedback type='invalid'>{errors.username}</Form.Control.Feedback>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword" isInvalid={!!errors.password}>
          <Form.Label>Пароль</Form.Label>
          <Form.Control type="password" value={password} onChange={e => setPassword(e.target.value)} isInvalid={!!errors.password} />
          <Form.Control.Feedback type='invalid'>{errors.password}</Form.Control.Feedback>
        </Form.Group>

        <Button variant="primary" onClick={handleSubmit} disabled={!isFormValid}>
          Войти
        </Button>
      </Form>
      <h>Нет аккаунта? <Link to='/register'>зарегистрироваться</Link></h>
    </div>
  );
}

export default Login;

import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import socket_backend from './../../Constants';

import './Auth.css';
import { Navigate } from 'react-router-dom';

function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
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

    if(confirmPassword !== password) {
      newErrors.password += '\nПароли не совпадают';
      formIsValid = false;
    }

    setErrors(newErrors);
    return formIsValid;
  };

  const handleSubmit = async event => {
    event.preventDefault();

    if(!validateForm()) {
      return;
    }

    try {
      const name = username;
      const responseCreateUser = await fetch("http://"+socket_backend+"/api/user", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, password })
      });
      console.log(responseCreateUser)
      if (responseCreateUser.status === 400) {
        throw new Error((await responseCreateUser.json()).detail);
      }

      const responseToken = await fetch("http://"+socket_backend+"/api/user/token", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, password })
      });

      if (!responseToken.ok) {
        throw new Error(responseToken.error);
      }

      const data = await responseToken.json();
      localStorage.setItem('accessToken', data.access_token);
      localStorage.setItem('refresh_token', data.refresh_token);
      window.location.href = '/';
    } catch (error) {
      setErrors({username: errors.username, password: errors.password + '\n' + error.message});
    }
  };

  if(localStorage.getItem('accessToken') != null) {
    return <Navigate to='/'/>
  }

  return (
    <div className='auth-container'>
      <Form>
        <Form.Group className='mb-3' controlId="formBasicUsername" isInvalid={!!errors.username}>
          <Form.Label>Имя пользователя</Form.Label>
          <Form.Control type='text' value={username} onChange={e => setUsername(e.target.value)} isInvalid={!!errors.username} />
          <Form.Control.Feedback type='invalid'>{errors.username}</Form.Control.Feedback>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword" isInvalid={!!errors.password}>
          <Form.Label>Введите пароль</Form.Label>
          <Form.Control type="password" value={password} onChange={e => setPassword(e.target.value)} isInvalid={!!errors.password} />
          <Form.Control.Feedback type='invalid'>{errors.password}</Form.Control.Feedback>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Повторите пароль</Form.Label>
          <Form.Control type="password" value={confirmPassword} onChange={e => setConfirmPassword(e.target.value)} isInvalid={!!errors.password} />
          <Form.Control.Feedback type='invalid'>{errors.password}</Form.Control.Feedback>
        </Form.Group>

        <Button variant="primary" onClick={handleSubmit} disabled={!isFormValid}>
          Зарегистрироваться
        </Button>
      </Form>
    </div>
  );
}

export default Register;

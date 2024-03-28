import React, { useState } from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { Link, Outlet } from 'react-router-dom';
import socket_backend from './../../Constants';

function NavigationBar() {
  const isLoggedIn = () => {
    const token = localStorage.getItem('accessToken');
    return token ? true : false;
  }

  const [name, setName] = useState('');
  const [isAdmin, setIsAdmin] = useState(false);

  async function setUserInfo() {
    const response = await fetch("http://"+socket_backend+"/api/user/token", {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('accessToken')
      }
    });
    if (response.status != 200) {
      return null
    }
    const data = await response.json()
    setName(data.name)
    setIsAdmin(data.role.toUpperCase() == 'АДМИНИСТРАТОР')
  }
  if(localStorage.getItem('accessToken')) {
    setUserInfo()
  }

  return (
    <Navbar bg="primary" data-bs-theme="dark">
      <Container>
        <Navbar.Brand as={Link} to="/">
          <img
            alt="logo"
            src="KOT.jpeg"
            width="45"
            height="45"
          />{" "}
          Канбан для нищих
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Nav className="ml-auto">
          {!isLoggedIn() && <Nav.Link as={Link} to="/login">Вход</Nav.Link>}
          {!isLoggedIn() && <Nav.Link as={Link} to="/register">Регистрация</Nav.Link>}
          {isLoggedIn() && isAdmin && <h5 style={{ color: 'blueviolet' }}>АДМИНИСТРАТОР</h5>}
          {isLoggedIn() && <h4>здравствуй, {name}</h4>}
          {isLoggedIn() && <Nav.Link as={Link} to="/logout">Выход</Nav.Link>}
        </Nav>
      </Container>
      <Outlet />
    </Navbar>
  );
}

export default NavigationBar;

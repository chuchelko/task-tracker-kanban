import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { Link, Outlet } from 'react-router-dom';

function NavigationBar() {
  const isLoggedIn = () => {
    const token = localStorage.getItem('token');
    return token ? true : false;
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
          {isLoggedIn() && <Nav.Link as={Link} to="/logout">Выход</Nav.Link>}
        </Nav>
      </Container>
      <Outlet/>
    </Navbar>
  );
}

export default NavigationBar;

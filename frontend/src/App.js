import React from 'react';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import NavigationBar from './components/NavigationBar/NavigationBar';
import Login from './components/Auth/Login';
import Logout from './components/Auth/Logout';
import Register from './components/Auth/Register';
import KanbanBoard from './components/KanbanBoard/KanbanBoard';

function NotFound(){
  return (
    <div>Нет такой страницы..</div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <NavigationBar />
      <Routes>
        <Route path="/" element={<Navigate to='/kanban'/>} />
        <Route path="/kanban" element={<KanbanBoard/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/logout" element={<Logout/>} />
        <Route path="/register" element={<Register/>} />
        <Route path="*" element={<NotFound/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NavigationBar from './components/NavigationBar/NavigationBar';
import Login from './components/Auth/Login';
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
        <Route path="/kanban" element={<KanbanBoard/>} />
        <Route path="/login" element={<Login/>} />
        <Route path="/register" element={<Register/>} />
        <Route path="*" element={<NotFound/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
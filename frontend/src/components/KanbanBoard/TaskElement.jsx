import { Button, Form, Modal } from "react-bootstrap";
import './KanbanBoard.css'
import { useState } from "react";

const TaskElement = ({ data, board, setBoards, boards }) => {

  const [isDrag, setIsDrag] = useState(false)

  const [show, setShow] = useState(false);
  
  const handleClose = async () => {
    console.log(formData)
    const response = await fetch('http://localhost:8000/api/task/', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('accessToken')
      },
      body: JSON.stringify(formData)
    });
    setShow(false);
  }

  const handleShow = async () => {
    const response = await fetch('http://localhost:8000/api/task/'+data.id, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('accessToken')
      }
    });
    if (response.status != 200) {
      return null
    }
    const resp = await response.json()
    setFormData(resp)
    setShow(true);
  }

  const [formData, setFormData] = useState({
    id: data.id,
    name: '',
    label_id: 0,
    description: '',
    participants: [],
    comments: []
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  function dragStartHandler(e, board, task) {
    console.log('start of dragging..')
    setIsDrag(true)
    e.dataTransfer.setData("taskId", task.id)
    e.dataTransfer.setData("boardId", board.id)
  }

  function dragEndHandler(e) {
    setIsDrag(false)
  }

  function truncateString(str, num) {
    if (str.length <= num) {
      return str
    }
    return str.slice(0, num) + '...'
  }

  function deleteClick(e) {
    // ЗАПРОС ЕБАНУТЬ
    const task = board.tasks.filter(t => t.id == data.id)[0]
    console.log(task)
    const taskIndex = board.tasks.indexOf(task)
    const newBoard = board.tasks.splice(taskIndex, 1)
    setBoards(boards.map(b => {
      if (b.id == newBoard.id) {
        return newBoard
      }
      else {
        return b
      }
    }))
  }


  return (
    <>
      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Окно редактирования данных</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group controlId="formName">
              <Form.Label>Имя</Form.Label>
              <Form.Control
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group controlId="formDescription">
              <Form.Label>Описание</Form.Label>
              <Form.Control
                as="textarea"
                name="description"
                value={formData.description}
                onChange={handleChange}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={setShow(false)}>
            Закрыть
          </Button>
          <Button variant="primary" onClick={handleClose}>
            Сохранить изменения
          </Button>
        </Modal.Footer>
      </Modal>
      <div className={isDrag ? "task-dragged" : "task"}
        draggable={true}
        onDragStart={(e) => dragStartHandler(e, board, data)}
        onDragEnd={(e) => dragEndHandler(e)}
      >
        <h className="task-text">{truncateString(data.name, 100)}</h>
        <Button className='task-button task-delete-button' onClick={e => deleteClick(e, boards, board, data)}><p>❌</p></Button>
        <Button className='task-button task-edit-button' onClick={handleShow}><p>✍️</p></Button>
      </div>
    </>
  );
};

export default TaskElement;

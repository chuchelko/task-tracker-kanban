import { Button } from "react-bootstrap";
import './KanbanBoard.css'
import { useState } from "react";

const TaskElement = ({ data, board, setBoards, boards }) => {

  const [isDrag, setIsDrag] = useState(false)

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
    <div className={isDrag ? "task-dragged" : "task"}
      draggable={true}
      onDragStart={(e) => dragStartHandler(e, board, data)}
      onDragEnd={(e) => dragEndHandler(e)}
    >
      <h className="task-text">{truncateString(data.name, 100)}</h>
      <Button className='task-button task-delete-button' onClick={e => deleteClick(e, boards, board, data)}><p>❌</p></Button>
      <Button className='task-button task-edit-button' onClick={}><p>✍️</p></Button>
    </div>
  );
};

export default TaskElement;

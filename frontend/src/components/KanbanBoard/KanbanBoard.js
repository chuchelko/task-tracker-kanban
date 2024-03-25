import React, { useState, useEffect } from 'react';
import { FormControl, Stack } from 'react-bootstrap';
import './KanbanBoard.css'
import TaskElement from './TaskElement';

function KanbanBoard() {
    const [boards, setBoards] = useState([]);
    // Получите labels из GET-запроса на бекенд
    useEffect(() => {
        // fetch('http://localhost:8000/api/labels')
        // //   .then(response => response.json())
        // .then(response => JSON.stringify(['В работе', 'Новая']))
        //   .then(data => {
        //     const initialColumns = {};
        //     data.forEach(label => {
        //       initialColumns[label] = [];
        //     });
        //     setColumns(initialColumns);
        //   });
        const boards = [
            { id: 1, text: 'Новые', tasks: [] },
            { id: 2, text: 'В работе', tasks: [{ id: 1, name: 'сделать фронт', description: 'опис' }] },
            { id: 3, text: 'Тестирование', tasks: [{ id: 1, name: 'прикрутить бэк', description: 'опис' }] },
            { id: 4, text: 'Ожидается подтверждение', tasks: [{ id: 1, name: 'выпить пива да.. пива выпить', description: 'опис' }] }
        ];
        setBoards(boards);
        console.log(boards);
    }, []);

    const handleInputChange = (event, labelId) => {
        const newTaskName = event.target.value;
        if(newTaskName.trim().length === 0) {
            return;
        }

        const newTask = { id: Date.now(), name: newTaskName };
        const labelIndex = boards.findIndex(label => label.id === labelId);

        if (labelIndex !== -1) {
            const updatedLabels = [...boards];
            updatedLabels[labelIndex].tasks.push(newTask);

            setBoards(updatedLabels);
        }
        event.target.value = '';

        console.log(`Creating new task in label ${labelId} with name ${newTaskName}`);
        console.log(boards);
    };

    function boardDragOver(e) {
        e.preventDefault();
    }

    function boardDrop(e, board) {
        const taskId = e.dataTransfer.getData("taskId");
        const oldBoardId = e.dataTransfer.getData("boardId");
        const oldBoard = boards.filter(b => b.id == oldBoardId)[0];
        const task = oldBoard.tasks.filter(t => t.id == taskId)[0];
        console.log(task)
        const currentIndex = oldBoard.tasks.indexOf(task)
        oldBoard.tasks.splice(currentIndex, 1)
        board.tasks.push(task)

        setBoards(boards.map(b => {
            if (b.id === board.id) {
                return board
            }
            if (b.id === oldBoard.id) {
                return oldBoard
            }
            return b
        }))
        console.log(boards);
    }

    return (
        <div style={{ borderRadius: '10px', overflow: 'hidden', margin: '30px', textAlign:'center'}}>
            <Stack gap={3} direction="horizontal" className="p-5 me-auto col-md-5">
                {boards.map(board =>
                    <Stack gap={3} onDragOver={e => boardDragOver(e)} onDrop={e => boardDrop(e, board)}>
                        <h className='board-name'>{board.text}</h>
                        <FormControl
                            type='text'
                            as="textarea"
                            className='newtask-formcontrol'
                            placeholder='Добавить'
                            onKeyDownCapture={(e) => {
                                if (e.key === 'Enter')
                                    handleInputChange(e, board.id);
                            }} />
                        {board.tasks.map(task =>
                            <TaskElement data={task} board={board} setBoards={setBoards} boards={boards}></TaskElement>
                        )}
                        <div></div>
                    </Stack>
                )}
            </Stack>
        </div>
    );
}

export default KanbanBoard;

import React, { useState, useEffect } from 'react';
import { FormControl, Stack } from 'react-bootstrap';
import './KanbanBoard.css'
import TaskElement from './TaskElement';
import { Navigate } from 'react-router-dom';

function KanbanBoard() {
    const [boards, setBoards] = useState([]);

    useEffect(() => {
        initBoards()
    }, []);

    async function initBoards() {
        const boards = await getBoardsFromBack()
        setBoards(boards);
        console.log(boards);
    }

    if (!localStorage.getItem('accessToken')) {
        return <Navigate to='/login'></Navigate>
    }

    async function getBoardsFromBack() {
        return await fetch('http://localhost:8000/api/label/get_all', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('accessToken')
            }
        }).then(async resp => {
            if (resp.status != 200) {
                return Error("Не удалось получить таблицу лейблов")
            }
            return await resp.json()
        })
    }

    const handleInputChange = async (event, labelId) => {
        const newTaskName = event.target.value;
        if (newTaskName.trim().length === 0) {
            return;
        }
        const userId = await fetch('http://localhost:8000/api/user', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('accessToken')
            }
        }).then(async resp => await resp.json()).then(resp => resp.id)

        await fetch('http://localhost:8000/api/task/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('accessToken')
            },
            body: JSON.stringify({ name: newTaskName, participant: userId, label_id: labelId })
        }).then(async resp => {
            const data = await resp.json()
            const newTask = { id: data.id, name: newTaskName };
            const labelIndex = boards.findIndex(label => label.id === labelId);

            if (labelIndex !== -1) {
                const updatedLabels = [...boards];
                updatedLabels[labelIndex].tasks.push(newTask);

                setBoards(updatedLabels);
            }
            event.target.value = '';

            console.log(`Creating new task in label ${labelId} with name ${newTaskName}`);
            console.log(boards);
            return resp
        })
    };

    function boardDragOver(e) {
        e.preventDefault();
    }

    async function boardDrop(e, board) {
        const taskId = e.dataTransfer.getData("taskId");
        const oldBoardId = e.dataTransfer.getData("boardId");
        const oldBoard = boards.filter(b => b.id == oldBoardId)[0];
        const task = oldBoard.tasks.filter(t => t.id == taskId)[0];
        await fetch('http://localhost:8000/api/task/', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('accessToken')
            },
            body: JSON.stringify({ id: taskId, label_id: board.id })
        }).then(resp => {
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
        })
    }

    return (
        <div style={{ borderRadius: '10px', overflow: 'hidden', margin: '30px', textAlign: 'center' }}>
            <Stack gap={3} direction="horizontal" className="p-5 me-auto col-md-5">
                {boards.map(board =>
                    <Stack gap={3} onDragOver={e => boardDragOver(e)} onDrop={e => boardDrop(e, board)}>
                        <h className='board-name'>{board.name}</h>
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
                            <TaskElement data={task} board={board} setBoards={setBoards} boards={boards} refreshBoards={initBoards}></TaskElement>
                        )}
                        <div></div>
                    </Stack>
                )}
            </Stack>
        </div>
    );
}

export default KanbanBoard;

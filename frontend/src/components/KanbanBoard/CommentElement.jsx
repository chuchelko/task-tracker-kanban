import React from "react";
import { Button, Stack } from "react-bootstrap";

const CommentElement = ({ comment, onDelete }) => {
    return (
        <div style={{borderRadius: '5px', border:'1px solid #ccc'}}>
            <Stack direction="horizontal" gap={3}>
                <p className="m-1 p-2">{comment.text}</p>
                <Button className="ms-auto" variant="danger" onClick={() => onDelete(comment)}>Удалить  </Button>
            </Stack>
        </div>

    );
};

export default CommentElement;
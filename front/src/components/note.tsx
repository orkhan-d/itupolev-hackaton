import React, {useState} from 'react';

export interface INote {
    id: number;
    title: string;
    teacher_id: number;
    teacher: string;
    info: string;
    done: boolean;
    deadline: Date;
}

const Note: React.FC<INote> = (note) => {
    // accordeon
    const [open, setOpen] = useState(false);

    const dateDay = note.deadline.getDate();
    const dateMonth = note.deadline.getMonth();
    const dateYear = note.deadline.getFullYear();

    const date = `${dateDay}.${dateMonth}.${dateYear}`;

    return (
        <div className={`note ${open ? "open" : ""}`}>
            <div className="note-title" onClick={() => setOpen(!open)}>
                <h3>{note.title}</h3>
            </div>
            {open &&
	            <>
		            <div className={"note-break"}/>
		            <div className="note-info">
			            <div className={"d-flex flex-row align-items-center justify-content-between gap-2 flex-wrap"}>
				            <p>{note.teacher}</p>
				            <p>{date}</p>
			            </div>
			            <p>{note.info}</p>
			            <button type={"button"} className={"note-btn"}>
                            {note.done ? "Выполнено" : "Не выполнено"}
			            </button>
		            </div>
	            </>
            }
        </div>
    );

};

export default Note;
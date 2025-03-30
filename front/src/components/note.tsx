import React, {useEffect, useState} from 'react';

export interface INote {
    id: number;
    title: string;
    teacher_id: number;
    teacher: string;
    info: string;
    done: boolean;
    deadline: Date;
}

interface ITimeTable {
    "id": number,
    "day_of_week": number,
    "lesson_number": number,
    "subject": {
        "name": string
    }
}

const Note: React.FC<INote> = (note) => {
    const [open, setOpen] = useState(false);

    const dateDay = note.deadline.getDate();
    const dateMonth = note.deadline.getMonth();
    const dateYear = note.deadline.getFullYear();

    const date = `${dateDay}.${dateMonth}.${dateYear}`;

    useEffect(() => {
        if (!open) {
            setTimetables([]);
        }
    }, [open]);

    const [timetables, setTimetables] = useState<ITimeTable[]>([]);

    const getTimetable = async () => {
        if (timetables.length > 0) {
            setTimetables([]);
            return;
        }
        const response = await fetch(`http://localhost:8000/timetable?teacher_id=${note.teacher_id}`);
        const data = await response.json();
        setTimetables(data);
    }

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
			            <button type={"button"} className={"note-btn"} onClick={getTimetable}>
                            {
                                timetables.length == 0
                                    ? "Показать расписание преподавателя"
                                    : "Скрыть расписание преподавателя"
                            }
			            </button>
                        {
                            timetables.length == 0
                                ? <></>
                                : <div className={"timetable"}>
                                    <h4>Расписание преподавателя</h4>
                                    <ul>
                                        {
                                            timetables.map((timetable) => {
                                                return (
                                                    <li key={timetable.id}>
                                                        <p>{timetable.subject.name}</p>
                                                        <p>{timetable.day_of_week} день недели</p>
                                                        <p>{timetable.lesson_number} пара</p>
                                                    </li>
                                                );
                                            })
                                        }
                                    </ul>
                                </div>
                        }
		            </div>
	            </>
            }
        </div>
    );

};

export default Note;
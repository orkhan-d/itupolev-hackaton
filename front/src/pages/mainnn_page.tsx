import Header from "../components/header.tsx";
import StudentInfo from "../components/student-info.tsx";
import Note from "../components/note.tsx";
import {useEffect, useState} from "react";
import {getNotes, INote} from "../api/notes.ts";
import {useStore} from "../store.ts";


const MainnnPage = () => {
    const [notes, setNotes] = useState<INote[]>([]);
    const student = useStore(s => s.student);

    useEffect(() => {
        getNotes().then((res) => {
            setNotes(res);
        });
    }, [student]);

    return (
        <div>
            <Header/>
            <StudentInfo full_name={student!.login}
                         stud_class={student!.class_.name}/>

            {
                notes.map((note) => (
                    <Note key={note.id}
                          id={note.id}
                          title={note.title}
                          teacher_id={note.teacher_id}
                          deadline={new Date(note.deadline)}
                          teacher={note.teacher.name}
                          info={note.content}
                          done={note.done}/>
                ))
            }
        </div>
    );
};

export default MainnnPage;
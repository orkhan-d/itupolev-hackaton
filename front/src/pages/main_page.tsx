import Header from "../components/header.tsx";
import StudentInfo from "../components/student-info.tsx";
import Note from "../components/note.tsx";


const MainPage = () => {
    return (
        <div>
            <Header/>
            <StudentInfo full_name={"Иванов Иван Иванович"}
                         stud_class={"ИВТ-21-1"}/>
            <Note id={1}
                  title={"Задание 1"}
                  teacher_id={1}
                  deadline={new Date()}
                  teacher={"Иванов Иван Иванович"}
                  info={"Сделать задание 1"}
                  done={false}/>
        </div>
    );
};

export default MainPage;
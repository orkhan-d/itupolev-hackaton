import React from 'react';
import Line from '../assets/line.svg';
import Avatar from '../assets/avatar.svg';

export interface IStudentInfo {
    full_name: string;
    stud_class: string;
}

const StudentInfo: React.FC<IStudentInfo> = ({full_name, stud_class}) => {
    return (
        <div className={"w-100 d-flex align-items-center justify-content-between p-3"}
             style={{
                 backgroundColor: "#86A5D9",
                 fontFamily: "Rubik",
                 lineHeight: "100%",
                 letterSpacing: "10%",
                 fontWeight: 400,
                 fontSize: "20px"
             }}>
            <div className={"d-flex flex-column gap-1 p-1"}>
                <p>{full_name}</p>
                <p>КАИ / {stud_class}</p>
                <img src={Line} alt=""/>
            </div>
            <img src={Avatar} alt="" className={"w-25"}/>
        </div>
    );
};

export default StudentInfo;
import Line from '../assets/line.svg';
import Avatar from '../assets/avatar.svg';
import React from "react";

interface Info {
    full_name: string,
    stud_class: string
}

const StudentInfo: React.FC<Info> = (props: Info) => {
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
                <p>{props.full_name}</p>
                <p>КАИ / {props.stud_class}</p>
                <img src={Line} alt=""/>
            </div>
            <img src={Avatar} alt="" className={"w-25"}/>
        </div>
    );
};

export default StudentInfo;
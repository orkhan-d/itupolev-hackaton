import {getInstance} from "./basic.ts";

const getNotes = async () => {
    const instance = getInstance();
    const res = await instance.get(
        `/notes?student_id=`
    );

    return res.data;
}
import {getInstance} from "./basic.ts";
import {useStore} from "../store.ts";

export interface INote {
    "content": string,
    "id": number,
    "teacher_id": number,
    "deadline": string,
    "title": string,
    "student_id": number,
    "done": boolean,
    "teacher": {
        name: string
    }
}

export const getNotes = async () => {
    const instance = getInstance();
    const res = await instance.get(
        `/notes?student_id=${useStore.getState().student!.id}`
    );

    return res.data as INote[];
}
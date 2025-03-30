import {getInstance} from "./basic.ts";
import {useStore} from "../store.ts";

export interface IStudentInfo {
    "id": number,
    "class_id": number,
    "password": string,
    "login": string,
    class_: {
        name: string
    }
}

export const login = async (login: string, password: string) => {
    const instance = getInstance();
    const res = await instance.post(
        `/autorisation?login=${login}&password=${password}`,
    );

    useStore.setState({student: res.data as IStudentInfo});

    return res.data as IStudentInfo;
}
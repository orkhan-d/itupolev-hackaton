import {getInstance} from "./basic.ts";

export interface IStudentInfo {
    id: number;
    full_name: string;
    stud_class: string;
}

export const login = async (login: string, password: string) => {
    const instance = getInstance();
    const res = await instance.post(
        `/autorisation`,
        {
            login,
            password
        }
    );

    return res.data as IStudentInfo;
}
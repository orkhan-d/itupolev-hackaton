import { create } from 'zustand'
import {IStudentInfo} from "./api/auth.ts";


export const useStore = create<{student: IStudentInfo | null}>()(() => ({
    student: null,
}))
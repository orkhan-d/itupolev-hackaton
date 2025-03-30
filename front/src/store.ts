import { create } from 'zustand'

type StudentStore = {
    s
}

const useStore = create<Store>()((set) => ({
    count: 1,
    inc: () => set((state) => ({ count: state.count + 1 })),
}))
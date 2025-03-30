// id
// title
// content
// teacher
// done
// deadline

import axios from "axios";

export const getInstance = () => {
    return axios.create({
        baseURL: 'http://127.0.0.1:8000',
    });
}
import {useEffect} from "react";
import {useStore} from "../store.ts";
import {login} from "../api/auth.ts";
import {useNavigate, useSearchParams} from "react-router-dom";


const MainPage = () => {
    const student = useStore(s => s.student);
    const [params] = useSearchParams();

    const nav = useNavigate();


    useEffect(() => {
        if (student === null) {
            (async () => {
                if (params.get('login') !== null && params.get('password') !== null) {
                    await login(params.get('login')!, params.get('password')!);
                    nav('/main');
                }
            })()
        }
    }, [params, student]);

    return (
        <div className={"d-flex align-items-center justify-content-center"}>
            <p>Loading</p>
        </div>
    );
};

export default MainPage;
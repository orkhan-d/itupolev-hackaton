import './App.css'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import MainPage from "./pages/main_page.tsx";
import Navbar from "./components/navbar.tsx";

function App() {
  return (
    <>
        <BrowserRouter>
            <div className="content">
                <Routes>
                    <Route path={"/"} element={<MainPage/>}/>
                </Routes>
            </div>
            <Navbar/>
        </BrowserRouter>
    </>
  )
}

export default App

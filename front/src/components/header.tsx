import Logo from '../assets/logo.svg';
import {HiMenu} from "react-icons/hi";

const Header = () => {
    return (
        <div className={"d-flex align-items-center justify-content-between px-3 py-2"}
        style={{
            backgroundColor: "#E7ECEF",
        }}>
            <img src={Logo} alt=""/>
            <HiMenu size={40} color={"#86A5D9"}/>
        </div>
    );
};

export default Header;
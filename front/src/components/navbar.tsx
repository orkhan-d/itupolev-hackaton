import {Link} from "react-router-dom";
import {BiArchive, BiPlay} from "react-icons/bi";
import {GiAchievement} from "react-icons/gi";
import {FiPlus} from "react-icons/fi";

const Navbar = () => {
    return (
        <div className={"my-navbar"}>
            <Link to={"/archive"} className={"navbar-item"}>
                <div>
                    <BiArchive color={"#000"} size={35}/>
                </div>
            </Link>
            <Link to={"/clicker"} className={"navbar-item"}>
                <div>
                    <BiPlay color={"#000"} size={35}/>
                </div>
            </Link>
            <Link to={"/achievements"} className={"navbar-item"}>
                <div>
                    <GiAchievement color={"#000"} size={35}/>
                </div>
            </Link>
            <Link to={"/edit"} className={"navbar-item"}>
                <div>
                    <FiPlus color={"#000"} size={35}/>
                </div>
            </Link>
        </div>
    );
};

export default Navbar;
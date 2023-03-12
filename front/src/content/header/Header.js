import React from "react";
import Logo from "./Logo";
import RightButtons from "./RightButtons";
import './Header.css';


const Header = () => (
    <div className="Header">
        <Logo textName={"Places KemSU"}/>
        <RightButtons />
    </div>

);

export default Header;





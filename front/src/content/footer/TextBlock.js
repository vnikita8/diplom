import { render } from "@testing-library/react";
import React from "react";
import Elements from "./Elements";

const TextBlock = (props) => (
    <div className="TextBlock">
        <p className="TextBlockHeader">{props.header}</p>
        <hr className="BlockTextLine"></hr>
        <Elements one="Да" />
        
    </div>

);


export default TextBlock;



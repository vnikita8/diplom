import React from "react";
import TextBlock from "./TextBlock";
import "./Footer.css";


const elementsOne = ["Главная страница", "Вакантные места", "Регистрация", "Вход"]
const elementsTwo = ["Главная страница", "Вакантные места", "Регистрация", "Вход"]

const Footer = () => (
    <div className="Footer">
        <TextBlock header="Полезные ссылки" elements = {elementsOne}/>
        <TextBlock header="Контактная информация" elements = {elementsTwo}/>
    </div>
);


export default Footer;
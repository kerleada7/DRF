import React from 'react';
import {Link} from "react-router-dom";

const Menu = () => {
    return (
        <ul>
            <li><Link to='/'>Users</Link></li>
            <li><Link to='/projects'>Projects</Link></li>
            <li><Link to='/todos'>ToDos</Link></li>
        </ul>
    )
}

export default Menu
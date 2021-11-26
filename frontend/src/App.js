
import React from 'react'
import axios from 'axios'

import Menu from './components/Menu';
import UserList from './components/Users';
import Footer from './components/Footer';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://localhost:8000/api/users/')
            .then(response => {
                this.setState(
                    {
                        'users': response.data
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <Menu/>
                <hr/>
                <UserList users={this.state.users}/>
                <hr/>
                <Footer/>
            </div>
        )
    }
}

export default App;
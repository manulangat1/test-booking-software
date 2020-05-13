import React from 'react'
import ReactDOM from 'react-dom'

import {Provider} from 'react-redux'
import store from '../store'
class App extends React.Component{
    render(){
        return(
            <Provider store={store}>
            <main>
                <h1>hey there</h1>
            </main>
            </Provider>
        )
    }
}
ReactDOM.render(<App />,document.getElementById("app"))
import React, { Component } from 'react';
import './config/globalVariables';
import Routes from './routes';
import './config/statusBarConfig';

export default class App extends Component {
    render(){
        return <Routes />;
    }
}
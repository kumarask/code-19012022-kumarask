import './App.css';
import React, { Component } from 'react'
import { Container } from "semantic-ui-react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from 'react-router-dom';

import Forms from './Components/Forms';


class App extends Component {
  render() {
    return (
      <Container>
        <Router>
          <Routes>
            <Route exact path='/' element={<Forms />}></Route>
          </Routes>
        </Router>
      </Container>
    );
  }
}

export default App;

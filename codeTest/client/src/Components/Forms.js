import React, { Component } from 'react'
import { Form } from 'semantic-ui-react'
import Quote from './Quote'


export default class Forms extends Component {
    state = { teamName: "", roleName: "" }

    handleSubmit = (event) => {

        event.preventDefault();
        const requestData = {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(this.state),
        }
        fetch('http://localhost:5000/createRecords', requestData)
        .then(response => response.json())
        .then(result => {
          console.log('Success:', result);
        })
        .catch(error => {
          console.error('Error:', error);
        });

        this.setState({teamName: "", roleName: ""})
    }

    handleChange = (e, { name, value }) => this.setState({ [name]: value })

    render() {
        const { teamName, roleName } = this.state

        return (
            <Form 
                onSubmit={this.handleSubmit}
            >
            <Quote header="Create New Data"/>
            <br />
            <br />
            <Form.Group widths='equal'>
                <Form.Input 
                    fluid 
                    label='Team Name' 
                    placeholder='Team name' 
                    type="text"
                    name="teamName"
                    value={teamName}    
                    onChange={this.handleChange}
                    required
                />
                <Form.Input 
                    fluid 
                    label='Role Name' 
                    placeholder='Role Name' 
                    type="text"
                    name="roleName"
                    value={roleName} 
                    onChange={this.handleChange}
                    required
                />
            </Form.Group>
            <Form.Button>Update</Form.Button>
            </Form>
        )
    }
}

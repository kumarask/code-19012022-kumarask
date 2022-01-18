
import React, { Component } from 'react';
import { Button, Container, Header, Segment } from 'semantic-ui-react'


export default class Quote extends Component {
    render () { 
        let buttonHTML = (this.props.link) ? <Button link={this.props.link}>Learn more</Button> : '';
    
        return (
            <Segment style={{ padding: '2em 0em' }} vertical>
                <Header as='h3' style={{ fontSize: '2em' }}>{this.props.header}</Header>
                <div style={{ fontSize: '1.33em' }}>
                    {this.props.content}
                </div>
                {buttonHTML}
            </Segment>
        );
    }
}
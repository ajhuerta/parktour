import React from 'react'
import {makeStyles} from '@material-ui/core/styles';
import Login from './Login';
const useStyles = makeStyles((theme) => ({
root:{
    height: '100vh',
},
}));
export default function ParkToVisit(){
    const classes = useStyles();
    return(
        <div className = {classes.root}>
        </div>
    );
}
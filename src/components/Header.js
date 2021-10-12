import React, { useEffect, useState } from 'react'
import { AppBar, Collapse, IconButton, makeStyles } from '@material-ui/core';
import { Toolbar } from '@material-ui/core';
import SortIcon from '@material-ui/icons/Sort';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Login from "./Login";
const useStyles = makeStyles((theme) => ({
root: {
    display: 'flex',
    justifyContent: 'right',
    alignItems: 'center',
    height: '100vh',
    fontFamiliy: 'Domine',
},
appbar: {
    background: 'none',
    fontFamiliy: 'Domine',
},
appbarTitle: {
    flexGrow: '1',
},
appbarWrapper: {
    width: '80%',
    margin: '0 auto',
},
colorText: {
    color: '#5AFF3D',
},
icon: {
    color: '#fff',
    fontSize: '2rem',
},
container: {
    textAlign: 'center',
},
title:{
    color: '#fff',
    fontSize: '4.5rem'
},
goDown: {
    color: '#5AFF3D',
    fontSize: '2rem',
},
}));
export default function Header(){
    const classes = useStyles();
    const [checked,setChecked] = useState(false);
    useEffect(() =>{
        setChecked(true);
    },[])
    return (
    <div  className = {classes.root}>
        <AppBar className = {classes.appbar} elevation = {0}>
            <Toolbar className = {classes.appbarWrapper}>
            <h1 className = {classes.appbarTitle}>
                ParkT'<span className = {classes.colorText}>our</span>
                </h1>
            <IconButton>
                <SortIcon className = {classes.icon}/>
            </IconButton>
            </Toolbar>
        </AppBar>
        <Collapse in = {checked} {... (checked ? {timeout: 1000} : {})} collapsedHeight = {50}>
        <div className = {classes.container}>
            <h1 className = {classes.title}>Welcome to your <br/> 
            <span className = {classes.colorText}>next destiniation.</span></h1>
            <IconButton>
                <ExpandMoreIcon className = {classes.goDown} />
            </IconButton>
        </div>
        </Collapse>
    </div>
    );
}
import React from 'react'
import { AppBar, IconButton, makeStyles } from '@material-ui/core';
import { Toolbar } from '@material-ui/core';
import SortIcon from '@material-ui/icons/Sort';


const useStyles = makeStyles((theme) => ({
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
}));
export default function Header(){
    const classes = useStyles();
    return <div>
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
    </div>;
}
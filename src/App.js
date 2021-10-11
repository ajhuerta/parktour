import React from 'react';
import { makeStyles } from '@material-ui/core';
import { CssBaseline } from '@material-ui/core';
import Header from './components/Header';

const useStyles = makeStyles((theme) => ({
  root:{
    height: '100vh',
    backgroundImage: `url(${process.env.PUBLIC_URL + '/assets/flatten.jpg'})`,
    backgroundRepeat: "no-repeat",
    backgroundSize: 'cover',
  },
}));
export default function () {
  const classes = useStyles();
  return (
    <div className = {classes.root}>
     <CssBaseline />
     <Header/>
    </div>
  );
}

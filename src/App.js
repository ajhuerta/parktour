import React from 'react';
import { makeStyles } from '@material-ui/core';
import { CssBaseline } from '@material-ui/core';
import Header from './components/Header';
import ParkToVisit from './components/ParkToVisit';
import Login from "./components/Login";

const useStyles = makeStyles((theme) => ({
  root:{
    height: '100vh',
    backgroundImage: `url(${process.env.PUBLIC_URL + '/assets/flatten.jpg'})`,
    backgroundRepeat: "no-repeat",
    backgroundSize: 'cover',
  },
}));
export default function App() {
  const classes = useStyles();
  return (
    <div className = {classes.root}>
     <CssBaseline />
     <Header/>
     <ParkToVisit/>
     <Login/>
    </div>
  );
}

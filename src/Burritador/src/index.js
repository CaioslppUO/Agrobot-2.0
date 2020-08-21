import React from 'react';
import './config/globalVariables';
import Routes from './routes';

console.reportErrorsAsExceptions = false;

export default function App() {
  return <Routes />;
}

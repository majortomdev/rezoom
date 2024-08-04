import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Login from "./components/Login";
import UrlobjectList from "./components/UrlobjectList";

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login" Component={Login} />
        <Route path="/urlobjects" Component={UrlobjectList} />
      </Switch>
    </Router>
  );
}

export default App;

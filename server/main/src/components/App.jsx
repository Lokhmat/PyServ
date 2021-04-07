import React, { Component } from 'react';
import classNames from 'classnames/bind'
import styles from "./App.module.scss"

const cx = classNames.bind(styles);

const spanStyles = {
  color: "green",
  borderColor: "#00f"
};

class App extends Component {
  
  
  render() {
    return (
      <div className={cx("DIV")} style={spanStyles}>Hello world</div>
    );
  }
}

export default App;

//const container = document.getElementById("app");
//render(<App />, container);
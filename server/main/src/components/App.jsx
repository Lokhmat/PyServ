import React from 'react';
import classNames from 'classnames/bind'
import styles from "./App.module.scss"

const cx = classNames.bind(styles);

const spanStyles = {
  color: "green",
  borderColor: "#00f"
};

class App extends React.Component {
  
  
  printlog = () =>{
    console.log("Oh, hi Mark!")
  }

  render() {
    return (
      <div>
      <div className={cx("test")}>Hello world</div>
      <button className={cx("test")} onClick = {this.printlog}>Click me!</button>
      </div>
    );
  }
}

export default App;

// import Button from "./Button";
// import styles from "./App.module.css";
import { useState, useEffect } from "react";
function App() {
  const [counter, setValue] = useState(0);
  const [keyword, setKeyword] = useState("");
  const onClick = () => setValue((prev) => prev + 1);
  const onChange = (event) => setKeyword(event.target.value);
  console.log('i run all the time');
  useEffect(() => {
    console.log("i run only once");
  }, []);
  useEffect(() => {
    if (keyword !== "" && keyword.length > 5) {
      console.log("i run when 'keyword' changes");
    }
  }, [keyword]);
  useEffect(() => {
    if (counter !== 0) {
      console.log("i run when 'counter' changes")
    }
  }, [counter]);
  useEffect(() => {
    console.log("i run when keyword & counter change");
  }, [keyword, counter]);
  return (
    <div>
      {/* <h1 className={styles.title}>Welcome back!!!!</h1>
      <Button text={"Continue"} /> */}
      <input type="text" onChange={onChange} placeholder="Search here..." />
      <h1>{counter}</h1>
      <button onClick={onClick}>Click me</button>
    </div>
  );
}

export default App;

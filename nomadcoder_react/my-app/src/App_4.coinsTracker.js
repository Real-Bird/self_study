import { useState, useEffect } from "react";
// https://api.coinpaprika.com/v1/tickers
function App() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);
  const [money, setMoney] = useState(0);
  const onChange = (event) => setMoney(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault();
    console.log()
  }
  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
      .then((response) => response.json())
      .then((json) => {
        setCoins(json);
        setLoading(false);
      })
  }, [])
  return (
    <div>
      <h1>The Coins! {loading ? "" : `(${coins.length})`} </h1>
      <input onChange={onChange} value={money} type="number" placeholder="How many have you money?" /> USD
      {loading ? <strong>Loading...</strong> : (
        <select>
          {coins.map((coin) => (
            <option>
              {coin.name} ({coin.symbol}) : {money / coin.quotes.USD.price} EA
            </option>
          ))}
        </select>
      )}
    </div>
  );
}

export default App;

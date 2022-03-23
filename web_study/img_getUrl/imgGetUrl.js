const randomePage = Math.floor(Math.random() * 10);
const randomeIdx = Math.floor(Math.random() * 100);
const url = `https://picsum.photos/v2/list?page=${randomePage}&limit=100`;

fetch(url)
  .then((response) => response.json())
  .then((data) => console.log(data[randomeIdx].download_url));

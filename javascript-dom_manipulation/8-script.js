fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
.then(response => response.json())
.then(data => {
  const hello = data.hello;
  document.getElementById('hello').innerHTML = hello;
});

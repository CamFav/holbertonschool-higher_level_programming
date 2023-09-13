// Select the HTML ul element with id "list_movies"
var movieList = document.getElementById("list_movies");

// Define the URL for the API
var apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";

// Use the Fetch API to make a GET request to the API
fetch(apiUrl)
  .then(function (response) {
    // Check if the response status is OK (200)
    if (response.ok) {
      // Parse the JSON response
      return response.json();
    }
  })
    .then(function (data) {
        var movies = data.results;

    // Loop through the movies and create a list item for each title
    movies.forEach(function (movie) {
      var movieTitle = document.createElement("li");
      movieTitle.textContent = movie.title;
      movieList.appendChild(movieTitle);
    });
});

// Select the HTML tag with id "character"
var characterElement = document.getElementById("character");

// Define the URL for the API
var apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";

// Use the Fetch API to make a GET request to the API
fetch(apiUrl)
  .then(function (response) {
    // Check if the response status is OK (200)
    if (response.ok) {
      // Parse the JSON response
      return response.json();
    }})
  .then(function (data) {
    // Extract the character name from the JSON data
    var characterName = data.name;
    
    // Display the character name in the "character" element
    characterElement.textContent = characterName;
  });

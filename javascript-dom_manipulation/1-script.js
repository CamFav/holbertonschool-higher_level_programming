// Select the element with id "red_header"
var redHeaderElement = document.getElementById("red_header");

// Add a click event listener to the "red_header" element
redHeaderElement.addEventListener("click", function () {
  // Select the header element
  var headerElement = document.querySelector("header");

  // Update the text color of the header to red
  headerElement.style.color = "#FF0000";
});

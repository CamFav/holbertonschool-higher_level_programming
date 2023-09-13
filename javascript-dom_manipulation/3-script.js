// Select the element with id "toggle_header"
var toggleHeaderElement = document.getElementById("toggle_header");

// Add a click event listener to the "toggle_header" element
toggleHeaderElement.addEventListener("click", function () {
  // Select the header element
  var headerElement = document.querySelector("header");

  // Check if the header currently has the "red" class
  if (headerElement.classList.contains("red")) {
    // Remove the "red" class and add the "green" class
    headerElement.classList.remove("red");
    headerElement.classList.add("green");
  } else if (headerElement.classList.contains("green")) {
    // Remove the "green" class and add the "red" class
    headerElement.classList.remove("green");
    headerElement.classList.add("red");
  } else {
    // If neither class is present, default to "red"
    headerElement.classList.add("red");
  }
});

// Select the element with id "add_item"
var addItemElement = document.getElementById("add_item");

// Add a click event listener to the "add_item" element
addItemElement.addEventListener("click", function () {
  // Create a new <li> element
  var newItem = document.createElement("li");
  
  // Set the text content of the <li> element to "Item"
  newItem.textContent = "Item";
  
  // Select the <ul> element with class "my_list"
  var myList = document.querySelector(".my_list");
  
  // Append the new <li> element to the <ul> element
  myList.appendChild(newItem);
});

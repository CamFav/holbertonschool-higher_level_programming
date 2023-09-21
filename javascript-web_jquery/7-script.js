$(document).ready(function() {
    $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function(name) {
        $('DIV#character').text(name.name);
    });
});
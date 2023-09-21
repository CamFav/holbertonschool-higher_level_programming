$(document).ready(function() {
    $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
        const movieTitles = data.results.map(movie => movie.title);
        $('UL#list_movies').html('<li>' + movieTitles.join('</li><li>') + '</li>');
    });
});
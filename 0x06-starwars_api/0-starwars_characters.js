#!/usr/bin/node

/**
 * Script that prints all characters of a Star Wars movie.
 * The first positional argument passed is the Movie ID.
 * Display one character name per line in the same order as the “characters” list in the /films/ endpoint.
 * You must use the Star wars API and the request module.
 */

const request = require('request');
const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const film = JSON.parse(body);
  const characters = film.characters;

  const promises = characters.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  Promise.all(promises)
    .then((characterNames) => {
      characterNames.forEach((name) => console.log(name));
    })
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
});

#!/usr/bin/node

const request = require('request');
const process = require('process');
function starWarsChars(movieId){
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request(url, {json: true}, (err, res, body) => {
        if(err){
            console.error("Error:", err);
            return;
        }
        if(res.statusCode !== 200){
            console.log(`Error: worng movie Id ${movieId}`);
            return;
        }
        const characters = body.characters;
        characters.forEach(charactersUrl => {
            request(charactersUrl, {json: true}, (err, res, bodyCharacters) => {
                if(err){
                    console.error("Error:", err);
                    return;
                }
                console.log(bodyCharacters.name);
            });
        });
    });
}
if (process.argv.length < 3){
    console.log("Usage: node Script.js <movieId>");
    process.exit(1);
}
const movieId = process.argv[2];

starWarsChars(movieId);

#!/usr/bin/node
// This script prints all characters of a Star Wars movie
const axios = require('axios');

const getperson = async (url) => {
  const name = await axios.get(url);
  return (name.data.name);
};

const getAllPerson = async (url) => {
  const resp = await axios.get(url);
  for (const character of resp.data.characters) {
    const newCaracter = await getperson(character);
    console.log(newCaracter);
  }
};

getAllPerson(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`);

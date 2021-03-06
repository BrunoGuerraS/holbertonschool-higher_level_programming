#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');
const [url, filePath] = process.argv.slice(2);

axios.get(url)
  .then(({ data }) => {
    fs.writeFile(filePath, data, 'utf8', err => {
      if (err) console.log(err.message);
    });
  })
  .catch(({ mess }) => console.log(mess));

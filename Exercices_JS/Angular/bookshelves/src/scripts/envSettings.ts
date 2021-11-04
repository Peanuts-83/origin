const { writeFile } = require('fs');
const { argv } = require('yargs');
require('dotenv').config();  // read .env

const environment = argv.environment;
const isProduction = environment === 'prod';

const targetPath = isProduction ?
  './src/environments/environment.prod.ts'
  :
  './src/environments/environment.ts';

const environmentFileContent =
`export const environment = {
  production: ${isProduction},
  apiKey: '${process.env.API_KEY}',
  authDomain: '${process.env.AUTH_DOMAIN}',
  databaseURL: '${process.env.DATABASE_URL}',
  projectId: '${process.env.PROJECT_ID}',
  storageBucket: '${process.env.STORAGE_BUCKET}',
  messagingSenderId: '${process.env.MSG_SENDER_ID}',
  appId: '${process.env.APP_ID}',
  measurementId: '${process.env.MSRT_ID}'
}`;

writeFile(targetPath, environmentFileContent, function (err) {
  if (err) {
    console.log(err);
  }
})
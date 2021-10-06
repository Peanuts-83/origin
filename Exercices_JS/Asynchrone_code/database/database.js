// centralDB //
let user1 = { id: 1, username: 'Toto83', age: 18, country: 'France' },
  user2 = { id: 2, username: 'Billou', age: 22, country: 'UK' },
  user3 = { id: 3, username: 'Aida88', age: 23, country: 'Belgium' },
  user4 = { id: 4, username: 'TonyIok', age: 15, country: 'Swiss' },
  user5 = { id: 5, username: 'Aisa-23', age: 27, country: 'Mali' };
const db1 = [user1, user2],
  db2 = [user3],
  db3 = [user4, user5];
const centralServer = { db1: db1, db2: db2, db3: db3 };

// vaultDB //
let user1s = { id: 1, fname: 'Tom', lname: 'Rank', email: 'aas@ds.fr' },
  user2s = { id: 2, fname: 'Bill', lname: 'Nami', email: 'dza@sff.uk' },
  user3s = { id: 3, fname: 'Susan', lname: 'Sarandon', email: 'qdd@c.be' },
  user4s = { id: 4, fname: 'Tony', lname: 'Ioka', email: 'asdzaz@dsqsds.sw' },
  user5s = { id: 5, fname: 'Aisa', lname: 'Ndogo', email: 'sdlkfd@sas.ma' };
const db1s = [/*user3s,*/ user4s],
  db2s = [user1s],
  db3s = [user2s, user5s];
const vaultServer = { db1s: db1s, db2s: db2s, db3s: db3s };

const users = {
  user1: user1,
  user2: user2,
  user3: user3,
  user4: user4,
  user5: user5,
  user1s: user1s,
  user2s: user2s,
  user3s: user3s,
  user4s: user4s,
  user5s: user5s,
};

// db Promises
function central(id, server) {
  return new Promise((resolve, reject) => {
    // dbSelector //
    function whichDb(id, server) {
      for (let db in server) {
        if (server[db].includes(users['user' + id])) {
          return db;
        }
      }
      return null;
    }
    setTimeout(() => {
      if (whichDb(id, server) !== null) {
        resolve(whichDb(id, server));
      } else {
        reject('Error from central');
      }
    }, 500);
  });
}

function db(id, dbId) {
  return new Promise((resolve, reject) => {
    function dbData(id, dbId) {
      for (let user of dbId) {
        if (user['id'] === id) {
          return user;
        }
      }
      return null;
    }
    setTimeout(() => {
      if (dbData(id, dbId) !== null) {
        resolve(dbData(id, dbId));
      } else {
        reject('Error from ' + dbId);
      }
    }, 500);
  });
}

function vault(id, server) {
  return new Promise((resolve, reject) => {
    // dbSelector //
    function whichDb(id, server) {
      for (let db in server) {
        if (server[db].includes(users['user' + id + 's'])) {
          return db;
        }
      }
      return null;
    }
    setTimeout(() => {
      if (whichDb(id, server) !== null) {
        resolve(whichDb(id, server));
      } else {
        reject('Error from vault');
      }
    }, 1500);
  });
}

// Request user
async function user(id) {
  const dbs = {
    db1: db1,
    db2: db2,
    db3: db3,
    db1s: db1s,
    db2s: db2s,
    db3s: db3s,
  };

  try {
    let data = ([
      await central(id, centralServer)
        .catch((error) => Promise.reject(error))
        .then((data) =>
          db(id, dbs[data]).catch((error) => Promise.reject(error))
        ),
      await vault(id, vaultServer)
        .catch((error) => Promise.reject(error))
        .then((data) =>
          db(id, dbs[data]).catch((error) => Promise.reject(error))
        ),
    ]);
  
      return ({
          id: id,
          username: data[0].username,
          age: data[0].age,
          country: data[0].country,
          firstname: data[1].fname,
          lastname: data[1].lname,
          email: data[1].email,
        });
  } catch(error) {
    throw error;
  }
}

user(5)
  .then((data) => console.log('Result: ', data))
  .catch((error) => console.log(error));
user(9)
  .then((data) => console.log('Result: ', data))
  .catch((error) => console.log(error));
user(3)
  .then((data) => console.log('Promise result: ', data))
  .catch((error) => console.log(error));

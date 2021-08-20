// chain of asynchrounous calls with promises
new Promise((resolve, reject) => setTimeout(() => resolve(1), 1000))
  .then((result) => {
    console.log(result);
    return new Promise((resolve, reject) =>
      setTimeout(() => resolve(result * 2), 200)
    );
  })
  .then((result) => {
    console.log(result);
    return new Promise((resolve) =>
      setTimeout(() => resolve(result * 2), 200)
    );
  })
  .then((result) => {
    console.log(result);
    return new Promise((resolve) =>
      setTimeout(() => resolve(result * 2), 200)
    );
  })
  .then((result) => {
    console.log(result);
    return new Promise((resolve, reject) =>
      setTimeout(() => reject(new Error("Can't go through...")), 200)
    );
  })
// single catch at the end of .then chain for getting any Error
  .catch((result) => {
  console.log(result.name);
  console.log(result.message);
});

/**
 *
 * EXERCISE 1
 *
 * @param {*} promise
 * @param {*} transformer
 * @returns {Promise}
 */
function mapPromise(promise, transformer){
  return new Promise((resolve, reject) => {
    /* IMPLEMENT ME!! */
    promise
      .then(res => transformer(res))
      .then(res => resolve(res))
      .catch(err => reject(err));
  });
}

/**
 *
 * EXERCISE 2
 *
 * @param {Promise<number | string>} numberPromise
 * @returns {Promise<number>}
 */
function squarePromise(numberPromise){
  return numberPromise
    .then(res => {
      if (typeof res === 'string') {
        if (!isNaN(parseInt(res))) {
          return Math.pow(parseInt(res), 2);
        }
      throw(`Cannot convert '${res}' to a number!`);
      }
      return Math.pow(res, 2);
    })
    .catch(err => { throw(err); });
}

/**
 * EXERCISE 3
 *
 * @param {Promise<number | string>} numberPromise
 * @returns {Promise<number>}
 */
function squarePromiseOrZero(promise){
  return squarePromise(promise)
    .catch(() => 0);
}

/**
 * EXERCISE 4
 *
 * @param {Promise} promise
 * @returns {Promise}
 */
function switcheroo(promise){
  return promise.then(
    res =>  { throw(res); },
    err => { return err; }
  );
}

/**
 * @callback consumer
 * @param {*} value
 */

/**
 * @callback handler
 * @param {*} error
 */

module.exports = {
  mapPromise,
  squarePromise,
  squarePromiseOrZero,
  switcheroo,
};
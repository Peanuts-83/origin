// we'll make worker.slow caching
let worker = {
  someMethod() {
    return 10;
  },
  slow(x,y) {
    // scary CPU-heavy task here
    console.log('Called with ' + x +' & '+ y);
    return x+y; // (*)
  },
};
// same code as before
function cachingDecorator(func) {
  let cache = new Map();
  return function (...args) {
    console.log(args)
    if (cache.has(args)) {
      return cache.get(args) + ' cached';
    }
    let result = func.call(this, ...args); // (**)
    console.log(cache)
    cache.set(args, result);
    return result;
  };
}
console.log(worker.slow(1,2)); // the original method works
worker.slow = cachingDecorator(worker.slow); // now make it caching
console.log(worker.slow(2,5));
console.log(worker.slow(2,5));

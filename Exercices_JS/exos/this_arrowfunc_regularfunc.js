function sayHi(who) {
  console.log('Hello, ' + who);
}

// wrapper
// this with arrow function
function defer(f, ms) {
  return function () {
    setTimeout(() => f.apply(this, arguments), ms);
  };
}

let sayHiDeferred = defer(sayHi, 1000);
sayHiDeferred('John'); // Hello, John after 2 seconds


// wrapper
// this & args with regular function
function defer2(f, ms) {
  return function (...args) {
    let ctx = this;
    setTimeout(function () {
      return f.apply(ctx, args);
    }, ms);
  };
}

let sayHiDeferred2 = defer2(sayHi, 2000);
sayHiDeferred2('Bill');


// add defer method to Function.prototype
function f(a,b) {
  console.log(a+b);
}
Function.prototype.defer = function wrap(ms) {
  let func = this;
  return function (...args) {
    setTimeout(() => func.apply(this,args), ms)
  }
}
f.defer(1000)(1,2); // shows 3 after 1 second

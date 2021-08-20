function f(x) {
  console.log(x);
}
// create wrappers
function delay(func, ms) {
  return function wrappers() {
    setTimeout(() => func.apply(this, arguments), ms);
  }
}

let f1000 = delay(f, 1000);
let f1500 = delay(f, 1500);
let f2500 = delay(f, 2500);
f1000('test1'); // shows "test" after 1000ms
f1500('test2'); // shows "test" after 1500ms
f2500('test3');
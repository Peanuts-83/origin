// camelize
camelize = (str) => {
  let res = '';
  for (s of str.split('_')){
    res += s[0].toUpperCase() + s.slice(1);
  }
  return res;
}
camelize('bg_color_is_blue');

// filter range
// Write a function filterRange(arr, a, b) that gets an array arr, looks for elements with values higher or equal to a and lower or equal to b and return a result as an array.
filterRange = (arr, a, b) => {
  let filtered = [];
  for (let i=0; i<=arr.length; i++) {
    if (arr[i]>=a && arr[i]<=b) {
      filtered.push(arr[i]);
    }
  }
  return filtered;
}
let arr = [5, 3, 8, 1];
let filtered = filterRange(arr, 1, 4);
filtered; // 3,1 (matching values)
arr; // 5,3,8,1 (not modified)

// Filter range "in place"
function filterRangeInPlace(arr, a, b){
  for (let i=0; i<arr.length; i++){
    if (arr[i]<a || arr[i]>b){
      arr.splice(i,1);
    }
  }
}
let arrayb = [5, 3, 8, 1];
filterRangeInPlace(arr, 1, 4); // removed the numbers except from 1 to 4
arr; // [3, 1]

// Sort in decreasing order
let arrayc = [5, 2, 1, -10, 8];
arrayc.sort(function(a,b){return(b-a)})
arrayc; // 8, 5, 2, 1, -10

// Copy and sort array
// We have an array of strings arr. We’d like to have a sorted copy of it, but keep arr unmodified.

function copySorted(arr){
  return arr.slice().sort();  // slice or concat copies array
}

let arrayd = ["HTML", "JavaScript", "CSS"];
let sorted = copySorted(arrayd);

sorted; // CSS, HTML, JavaScript
arrayd; // HTML, JavaScript, CSS (no changes)
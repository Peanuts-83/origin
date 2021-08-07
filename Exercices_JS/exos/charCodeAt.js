function rot13(str) {
    let res = '';
    for (let letter of str) {
      res +=
       (/\W|\s/g).test(letter) === true
          ? letter
          : letter.charCodeAt() <= 77
          ? String.fromCharCode(letter.charCodeAt() + 13)
          : String.fromCharCode(letter.charCodeAt() - 13);
    }
    return res;
  }
  
  rot13('SERR PBQR PNZC');
  rot13("SERR CVMMN!");
  
  'A'.charCodeAt();
  90 - 13;
  90 - 65;
  let a ='"';
  a.match(/\W/g);
  (/\W/g).test(a);
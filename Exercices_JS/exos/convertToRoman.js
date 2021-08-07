function convertToRoman(num) {
    const table = {
      1000: 'M',
      500: 'D',
      100: 'C',
      50: 'L',
      10: 'X',
      5: 'V',
      1: 'I',
    };
    let res = num
      .toString()
      .split('')
      .map((x) => Number(x));
    console.log(res);
  
    function romanize(num) {
      // num: 3000 / 400 / 90 / 6
      let romanTab = Object.keys(table)
        .reverse()
        .map((val) => Number(val));
      // [ 1000, 500, 100, 50, 10, 5, 1 ]
      // romans = Object.assign({}, romanTab);
      // {'0': 1000,'1': 500,'2': 100,'3': 50,'4': 10,'5': 5,'6': 1}
      console.log(num);
      for (let val of romanTab) {
        console.log(val);
        let res;
        if (num === val) {
          return table[val];
        } else if (num === val * 2) {
          return table[val].repeat(2);
        } else if (num === val * 3) {
          return table[val].repeat(3);
        } else if (num === (val * 9) / 10) {
          return table[romanTab[romanTab.indexOf(val) + 2]] + table[val];
        } else if (num === (val * 11) / 10 && val.toString()[0] == 1) {
          return table[val] + table[romanTab[romanTab.indexOf(val) + 2]] ;
        } else if (num === (val * 12) / 10 && val.toString()[0] == 1) {
          return table[val] + table[romanTab[romanTab.indexOf(val) + 2]].repeat(2) ;
        } else if (num === (val * 13) / 10 && val.toString()[0] == 1) {
          return table[val] + table[romanTab[romanTab.indexOf(val) + 2]].repeat(3) ;
        } else if (num === (val * 4) / 5 && val.toString()[0] == 5) {
          return table[romanTab[romanTab.indexOf(val) + 1]] + table[val];
        } else if (num === (val * 6) / 5 && val.toString()[0] == 5) {
          return table[val] + table[romanTab[romanTab.indexOf(val) + 1]];
        } else if (num === (val * 7) / 5 && val.toString()[0] == 5) {
          return table[val] + table[romanTab[romanTab.indexOf(val) + 1]].repeat(2);
        } else if (num === (val * 8) / 5 && val.toString()[0] == 5) {
          return table[val] + table[romanTab[romanTab.indexOf(val) + 1]].repeat(3);
      }}
    }
    
    let counter = 0;
    res = res
      .map(x => getVal(x))
      .map(x => romanize(x));
  
    function getVal(x) {
      counter++;
      console.log(x * Math.pow(10, res.length - counter));
      return x * Math.pow(10, res.length - counter);
    }
    
    return res.join('');
  }
  
  convertToRoman(44);
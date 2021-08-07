function telephoneCheck(str) {
    let reg1 = /^1?[\s\d]?\d{2,3}[\s-]?\d{3}[\s-]?\d{4}$/g,
      reg2 = /^1?\s?[(]\d{3}[)][\s-]?\d{3}[\s-]?\d{4}/g;
    console.log('reg1: ' + str.replace(reg1, ''));
    console.log('reg2: ' + str.replace(reg2, ''));
  
    let lenTest = str.replace(/[\s-()]/g, '');
    if (
      (lenTest.length != 10 && lenTest.length != 11) ||
      (str[0] != 1 && lenTest.length == 11)
    )
      return false;
  
    return str.replace(reg1, '') == ''
      ? true
      : str.replace(reg2, '') == ''
      ? true
      : false;
  }
  
  telephoneCheck('555-555-5555'); //true
  telephoneCheck('(555) 555-5555'); //true
  telephoneCheck('1 555-555-5555'); //true
  telephoneCheck('1 (555) 555-5555'); //true
  
  telephoneCheck('-1 (555) 555-5555'); //false
  telephoneCheck('(6054756961)'); //false
  telephoneCheck('55 55-55-555-5'); // false
  telephoneCheck('27576227382');//false
  
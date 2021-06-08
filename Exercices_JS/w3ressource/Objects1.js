let user = {
  name: 'John',
  surname: 'Smith'
}
user.name = 'Pete';
user;
delete user.name;
user;

//
isEmpty = (obj) => {
  for (let k in obj){
    return false;
  } 
  return true;
  
}
let obj = {};
console.log('query 1: ',obj)
isEmpty(obj);
obj.name = 'Gill';
console.log('query 2: ',obj)
isEmpty(obj);

//
let salaries = {
  John: 100,
  Ann: 160,
  Pete: 130
}
let sum = 0;
for (let val in salaries){
  sum += salaries[val];
}

//
let menu = {
  width: 200,
  height: 300,
  title: "My menu"
};
multiplyNumeric = (menu) => {
  for (let val in menu){
    if (typeof(menu[val]) === 'number'){
      console.log('yes');
      menu[val] *= 2;
    } else {
      console.log('no');
    }
  }
}
multiplyNumeric(menu);
menu;

//















// methods & getter/setter in constructor f()
function User(name, birthday) {
  this.name = name;
  this.birthday = birthday;
  this.age = () => {                        // age() method
    let today = new Date().getFullYear();
    return today - this.birthday.getFullYear();
  };
  Object.defineProperty(this, "age2", {    // age getter
    get() {
    let today = new Date().getFullYear();
    return today - this.birthday.getFullYear();      
    }
  })
}

let tom = new User('thomas', new Date(1975, 3, 22));
tom.name;
tom.birthday;
tom.age();
tom.age2;

let isa = new User('Isabelle', new Date('1970,12,30'));
isa.birthday;
isa.name;
isa.age();
isa.age2;
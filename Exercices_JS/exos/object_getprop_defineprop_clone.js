let user = {
  name: 'Tom',
};

let descr = Object.getOwnPropertyDescriptor(user, 'name');
JSON.stringify(descr, null, 2);

Object.defineProperty(user, 'surname', {
  value: 'Tadej',
  writable: true,
  enumerable: true,
});

Object.getOwnPropertyDescriptors(user);

let clone = Object.defineProperties({}, Object.getOwnPropertyDescriptors(user));

Object.getOwnPropertyDescriptors(clone);
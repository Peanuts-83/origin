interface Foo {
    arg1: string;
    arg2: number;
}

let a: Foo = {
    arg1: 'tom',
    arg2: 5,
}

class Bar {
    arg1: string;
    arg2: number;
}

const b: Bar = {
    arg1: 'aaa',
    arg2: 6
}
const c = new Bar
c.arg1 = 'eee'
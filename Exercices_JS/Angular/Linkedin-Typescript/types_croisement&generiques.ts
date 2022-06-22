// Croisement de type
let a = (value: Array<any> | string): void => console.log(value.length)

interface Int1 {
    prop1: any;
    prop2: any;
}

interface Int2 {
    prop3: any;
}

let b: Int1 & Int2 = {
    prop1: 15,
    prop2: 'azerty',
    prop3: 12,
}

let c: Int1 | Int2 = {
    // prop1: 15,
    // prop2: 'azerty',
    prop3: 12,
}

// types generiques - Type generique <T> de même type au début et à la fin
let z: <T>(v: T) => T[]  = value => [value]

interface IntGen <T> {
    prop1: T,
    prop2: T[]
}

let e: IntGen <number> = {
    prop1: "foo",                      // ne correspond pas au type generique <T> defini!
    prop2: [21,12]
}

class ClassGen <T> {
    constructor(public arg1: T, public arg2: T) {}

    toArray: () => T[] = () => [this.arg1, this.arg2]
}

let r = new ClassGen(1,2)
r.toArray
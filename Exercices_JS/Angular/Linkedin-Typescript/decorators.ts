// decorer classes, methodes, propriétés, accesseurs...

// Classe // decorateur de classe = function qui s'execute à chq instanciation de la classe
// Reçoit automatiquement le constructeur de la classe en argument
const d1 = (constructor) => console.log('Décorateur executé', constructor)
const d2: PropertyDecorator = (proto, name) => {
    console.log('PROTO', proto);
    console.log('NAME', name);
}

@d1
class ClassGen2 <T> {       // flag --experimentalDecorators dans bash au lancement
    constructor(public arg1: T, public arg2: T) {}

    @d2
    prop1: string = 'foo'
}

let q = new ClassGen2(1,2)
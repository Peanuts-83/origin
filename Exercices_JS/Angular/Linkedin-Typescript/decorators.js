// decorer classes, methodes, propriétés, accesseurs...
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
// Classe // decorateur de classe = function qui s'execute à chq instanciation de la classe
// Reçoit automatiquement le constructeur de la classe en argument
var d1 = function (constructor) { return console.log('Décorateur executé', constructor); };
var d2 = function (proto, name) {
    console.log('PROTO', proto);
    console.log('NAME', name);
};
var ClassGen2 = /** @class */ (function () {
    function ClassGen2(arg1, arg2) {
        this.arg1 = arg1;
        this.arg2 = arg2;
        this.pro1 = 'foo';
    }
    __decorate([
        d2
    ], ClassGen2.prototype, "pro1");
    ClassGen2 = __decorate([
        d1
    ], ClassGen2);
    return ClassGen2;
}());
var q = new ClassGen2(1, 2);

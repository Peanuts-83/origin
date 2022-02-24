class Shop {
    constructor() {
        this.chamallow = 510;
        this.carambar = 4;
    }
    pick(candyName, num) {
        return this[candyName] - num;
    }
    add(candyName, num) {
        return this[candyName] + num
    }
}
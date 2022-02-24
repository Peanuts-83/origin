describe ("Shop inventory", () => {
    let shop = new Shop();

    it('should detect how much candies decrease when taken from customer', () => {
        expect(shop.pick('chamallow', 20)).toEqual(490);
    })
    it('should detect how much candies are added by employee', () => {
        expect(shop.add('carambar', 600)).toEqual(604);
    })
    it('should detect pick in chamallow do not change carambar', () => {
        expect(shop.pick('chamallow', 20), shop['carambar']).toEqual(490, 4);
    })
})
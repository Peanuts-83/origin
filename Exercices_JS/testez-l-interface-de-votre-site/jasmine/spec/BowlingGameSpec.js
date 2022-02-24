describe('Bowling game', () => {
    let game;

    beforeEach(() => {
        game = new BowlingGame();
    })

    function rollMany(n, pins) {
        for (let i = 0; i<n; i++) {
            game.roll(pins);
        }
    }

    it('should calculate a gutter game', () => {
        rollMany(20, 0);
        expect(game.score()).toEqual(0);
    });
    it('should calculate a spare game', () => {
        rollMany(20, 10);
        expect(game.score()).toEqual(200);
    });
    it('should calculate a strike game', () => {
        rollMany(20, 15);
        expect(game.score()).toEqual(300);

    });
})
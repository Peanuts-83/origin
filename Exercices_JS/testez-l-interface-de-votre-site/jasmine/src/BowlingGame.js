class BowlingGame {
    constructor() {
        this.rolls = [];
        this.currentRoll = 0;
    }
    roll(pins) {
        this.rolls[this.currentRoll++] = pins;
    }
    score() {
        var score = 0;
        var frameIndex = 0;
        var self = this;

        function sumOfBallsInFrame() {
            return self.rolls[frameIndex] + self.rolls[frameIndex + 1];
        }

        for (var frame = 0; frame < 10; frame++) {
            score += sumOfBallsInFrame();
            frameIndex += 2;
        }
        return score;
    }
}

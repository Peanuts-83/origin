// CLASSES

class DepotScores {

  constructor(jury) {
    this.scores = {};
    this.scoreSum = {};
    this.countFullScores = 0;
    jury.forEach(arbitre => this.scores[arbitre.nom] = {})
  }

  sauverScores(arbitre, enfant, score) {
    this.scores[arbitre][enfant] = score;
    let fullScore = true;
    Object.keys(this.scores)
      .forEach(arbitre => {
        if (this.scores[arbitre][enfant] === undefined) {
          fullScore = false;
        }
      });

      if (fullScore) {
        let sum = this.totaliserScores(enfant);
        console.log(`***** ${enfant} obtient un total de ${sum} points *****`);
        this.scoreSum[enfant] = sum;
        this.countFullScores += 1;

        if (this.countFullScores === Object.keys(this.scores[arbitre]).length) {
          // Winner IS!
          let scoreMax = this.scoreSum[Object.keys(this.scoreSum)
          .reduce((a, b) => {
            return this.scoreSum[a] > this.scoreSum[b] ? a : b;
          })];
          let winner = Object.keys(this.scoreSum).filter(enfant => {
            return this.scoreSum[enfant] === scoreMax;
          })
          console.log(`\nle(s) gagnant(s):`)
          for (let i of winner) {
            console.log(`${winner} gagne avec ${this.scoreSum[winner]} points.`)
          }
        }
      }
  }

  totaliserScores(enfant) {
    let sum = Object.keys(this.scores)
      .reduce((total, arbitre) => {
        total += this.scores[arbitre][enfant];
        return total;
      }, 0);
    return sum;
  }
}


class Personne {
  constructor(nom) {
    this.nom = nom;
  }
}

class Arbitre extends Personne {
  constructor(nom) {
    super(nom);
  }

  coter(depotScores, enfant) {
    // let score = Math.round(Math.random() * 10),
    //     time = Math.round(Math.random() * 5) * 1000;
    this.interrogerArbitre()
      .then(res => {
        setTimeout(() => {
          if (res.time == 5000) {console.log(`Arbitre ${this.nom} distrait`);}
          console.log(`${enfant} obtient ${res.score} de la part de ${this.nom}!`);
          return depotScores.sauverScores(this.nom, enfant, res.score);
        }, res.time)
      });
  }

  interrogerArbitre() {
    return new Promise(resolve => {
      let time = Math.round(Math.random() * 10) *1000;
      if (time <= 5000) {
        let score = Math.round(Math.random() * 10);
        resolve ({score:score, time:time});
      } else {
        let score = Math.round(Math.random() * 5) + 5;
        resolve ({score:score, time:time});
      }
    })
  }
}


class Enfant extends Personne {
  constructor(nom) {
    super(nom);
  }

  obtenirScores(jury, scores) {
    let msg = [];
    jury.forEach((juge, i) => {
      let score = juge.coter(scores, this.nom);
      msg.push(`Vote de ${juge.nom} sur ${this.nom} ?`);
      scores.sauverScores(juge.nom, this.nom, score);
      if (i === jury.length - 1) {
        msg.forEach(msg => console.log(msg));
      }
    })
  }
}

// Instances
let enfants = [
  new Enfant('Andréa Maxence'),
  new Enfant('Ronan Vivien'),
  new Enfant('Demetrio Yasmin'),
  new Enfant('Kanya Lorenzo'),
  new Enfant('Claptrap Jessica'),
  new Enfant('Sung Li')
];

let jury = [
  new Arbitre('Faro Lindemans'),
  new Arbitre('Dave Gilmort'),
  new Arbitre('Angus Old'),
  new Arbitre('Jacques Hetchamp')
];

// Actions
let scores = new DepotScores(jury);
enfants.forEach(e => e.obtenirScores(jury, scores));

//setTimeout(() => console.log(scores), 2000)

// CLASSES

class DepotScores {

  constructor(jury) {
    this.scores = {};
    this.scoreSum = {};
    this.countFullScores = 0;
    jury.forEach(arbitre => this.scores[arbitre.nom] = {})
  }

  sauverScores(arbitre, enfant, score) {
    // Score enregistré
    this.scores[arbitre][enfant] = score;

    // Evaluation des scores de l'enfant
    let fullScore = true;
    Object.keys(this.scores)
      .forEach(arbitre => {
        if (this.scores[arbitre][enfant] === undefined) {
          fullScore = false;
        }
      });

      // les 4 arbitre ont voté pour l'enfant sélectionné
      if (fullScore) {
        let sum = this.totaliserScores(enfant);
        // ANSI code '\u001b[1;31m' to get result RED color ('\u001b[1;0m' for default)
        console.log(`***** ${enfant} obtient un total de \u001b[1;31m${sum}\u001b[1;0m points *****`);
        this.scoreSum[enfant] = sum;
        this.countFullScores += 1;

        // Tous les enfants ont reçu leurs votes
        if (this.countFullScores === enfants.length) {
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
            console.log(`\u001b[1;31m${i} gagne avec ${this.scoreSum[i]} points.`)
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

  async coter(enfant) {
    let res = this.interrogerArbitre();
    setTimeout(() => {
      return ([this.nom, enfant, res.score, res.time]);
    }, res.time)
    }

    interrogerArbitre() {
        let time = Math.round(Math.random() * 10) *1000;
        if (time <= 5000) {
          // Score si moins de 5 sec de HEAD BANGING
        let score = Math.round(Math.random() * 10);
        return ({score:score, time:time});
      } else {
        // Score si plus de 5 sec de HEAD BANGING
        let score = Math.round(Math.random() * 5) + 5;
        return ({score:score, time:time});
      }
  }
}


class Enfant extends Personne {
  constructor(nom) {
    super(nom);
  }

  async obtenirScores(jury, scores) {
    let msg = [];
    let promises = [];
    jury.forEach((arbitre, i) => {
      promises.push(arbitre.coter(this.nom));
      msg.push(`Vote de ${arbitre.nom} sur ${this.nom} ?`);
      if (i === jury.length - 1) {
        msg.forEach(msg => console.log(msg));
      }
    });

      Promise.all(promises)
      .then(res => {
        res.forEach(([arbitre, enfant, score, delay]) => {
          if (delay === 5000) {console.log(`Arbitre ${this.nom} distrait`);}
          console.log(`${enfant} obtient ${score} de la part de ${arbitre}!`);
          scores.sauverScores(arbitre, enfant, score);
        })
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

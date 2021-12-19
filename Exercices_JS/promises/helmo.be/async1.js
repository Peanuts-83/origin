// CLASSES

class DepotScores {

  constructor(jury) {
    this.scores = {};
    //this.jury = jury;
    jury.forEach(arbitre => this.scores[arbitre.nom] = {})
  }

  sauverScores(arbitre, enfant, score) {
    this.scores[arbitre][enfant] = score;
    for (enfant in arbitre) {
      
    }
    //console.log(this.scores);
  }

  totaliserScores(enfant) {
    let sum = 0;
    Object.keys(this.scores)
      .forEach(arbitre => {
        sum += arbitre[enfant];
      })
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
    let score = Math.round(Math.random() * 10),
        time = Math.round(Math.random() * 5) * 1000;
    setTimeout(() => {
      depotScores.sauverScores(this.nom, enfant, score);
      console.log(`${enfant} obtient ${score} de la part de ${this.nom}!`);
    }, time);
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

//setTimeout(() => console.log(scores), 10000)
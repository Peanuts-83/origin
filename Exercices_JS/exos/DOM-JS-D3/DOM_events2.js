// console.log(chanson);
// Structure de Chanson:
// - titre: string
// - auteur: string
// - paroles : [Couplet, Couplet, ...]

// Structure de Couplet:
// id : string
// type : string
// chanteur : string
// contenu: tableau contenant les lignes du couplet

// 1.

// 2.

// 3.

// 4. [optionnel]

let doc = document.createElement('div');
doc.classList.add('paroles');
document.body.prepend(doc);
let paroles = document.querySelector('.paroles');

let couplets = Object.values(chanson.paroles);
//alert(couplets.length);
//alert(Object.values(couplets[0].contenu));

couplets.forEach((e, index) => {
    let txt = Object.values(couplets[index].contenu).join('<br>');
    let pCouplet = document.createElement('p');
    pCouplet.innerHTML = txt;
    paroles.append(pCouplet);
})

let footer = document.createElement('footer');
footer.innerHTML = '© Copyright 2020 - IUT';
paroles.append(footer);
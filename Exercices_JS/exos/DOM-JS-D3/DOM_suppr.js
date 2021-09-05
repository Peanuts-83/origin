
// JS VERSION //
/*
document.querySelector('h1').innerHTML = 'Rick Astley - Never Gonna Give You Up';

let couplets = document.querySelectorAll('.couplet');
[...couplets].forEach(couplet => {
    let newCouplet = couplet.innerHTML.split('<br>');
    newCouplet.shift();
    couplet.innerHTML = newCouplet.join('<br>');
})

let refrains = document.querySelectorAll('.refrain');
[...refrains].forEach(refrain => {
    let newRefrain = refrain.innerHTML.split('<br>');
    newRefrain = newRefrain.map((e, i) => (i%2 != 0) ? e : null).filter(e => e != null);
    refrain.innerHTML = newRefrain.join('<br>');
})

document.getElementById('erreur').remove();

document.body.append(document.createElement('footer'));
document.querySelector('footer').innerHTML = '© Copyright 2020 - Nom';

*/


// D3js VERSION //
// 1
// on selectionne un element, on ajoute text
// d3.select('element').text('text');
// 2

// on selectionne tous les objets de la classe "une-classe"
d3.selectAll('.couplet').each(function () {
    // on applique cette operation pour chacun d'entre eux
    // "this" correspond à l'élement selectionné. par exemple: <p>
    //alert(this);
    this.childNodes[1].remove();
    this.childNodes[0].remove();

    // le but est de supprimer les deux premiers noeuds
    // indice : "this.firstChild" ou "this.childNodes[0]"
    // ps, n'oubliez pas le <br> en trop
    // pour supprimer un objet:
    //d3.select(objet).remove();
  });

  // 3
  // on selectionne tous elements de une-classe
  d3.selectAll('.refrain').each(function () {
    // pour chacun d'entre eux on sélectionne leur noeuds enfant
    d3.selectAll(this.childNodes)
      // on filtre les noeuds sélectionnés pour ne garder que les doublons
      .filter((_d, i) => Math.floor(i / 2) % 2 === 0)
      // on les supprime
      .remove();
  });

  // 4
  d3.select('#erreur').remove();
  // astuce : d3.select et .remove()
  // n'oubliez pas de # pour selectionner par id

  //5
  d3.select('body').append('footer')
  .text('© Copyright 2020 - Nom');
  //  astuce : on utilise append pour ajouter un element <footer> dans notre cas
  //  d3.select('body').append('footer');

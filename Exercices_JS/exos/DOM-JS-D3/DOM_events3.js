// D3 VERSION //
// Récupere la case "masquer les paroles"
const checkboxParoles = d3.select('#masquer-paroles');
// Récupère le div contenant les paroles
const divParoles = d3.select('#paroles');

// Attache une fonction à l'évènement "click" sur checkboxParoles
checkboxParoles.on('click', function () {
  // cette fonction est executée lorsque l'utilisateur clique sur checkboxParoles
  // d3.event.target contient l'élément cliqué (ici checkboxParoles dans notre cas)
  if (d3.event.target.checked) {
    divParoles.classed('hidden', true);
  } else {
    divParoles.classed('hidden', false);
  }
});


const checkboxRefrains = d3.select('#masquer-refrains');
const defRefrains = d3.selectAll('.definition');
const contRefrains = d3.selectAll('.contenu');

checkboxRefrains.on('click', function() {
    if (d3.event.target.checked) {
        defRefrains.classed('hidden', false);
        defRefrains.on('mouseover', function() {
            d3.select(this.parentNode).select('.contenu').classed('hidden', false);
        });
        defRefrains.on('mouseout', function() {
            d3.select(this.parentNode).select('.contenu').classed('hidden', true);
        });
        contRefrains.classed('hidden', true);

    } else {
        defRefrains.classed('hidden', true);
        contRefrains.classed('hidden', false);
    }
})
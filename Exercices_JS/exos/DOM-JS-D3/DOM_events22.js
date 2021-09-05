// D3 VERSION //
// Remplissage de la page
let auteur = chanson.auteur;
let titre = chanson.titre;
d3.select('body')
    .insert('h1', ':first-child')   // second arg -> before
    .html(`<small>${auteur}</small> ${titre}`);

let couplets = chanson.paroles;
d3.select('body')
    .insert('div', 'script')
    .attr('class', 'paroles')
    .selectAll('p')                  // enables <p> insertions at right place
    .data(couplets)
    .enter()
    .append('p').attr('class', function (d) {     // get 'choeur' or 'verset' attr
        return d.type;
    })
    .html(d => d.contenu.join('<br>'))
    ;

// CREATE 'Choeurs' callback
d3.selectAll('.choeur')
    .select(function () {        // insert before this in parentNode!
        return this.parentNode.insertBefore(document.createElement('span'), this);
    })
    .attr('class', 'callback hidden choeur')
    .text('Choeurs...');

// FOOTER
d3.select('body')
    .insert('footer', 'script')
    .text('© Copyright 2020 - IUT');

// FONCTIONS de masquage du texte
// Ajout des checkboxs de masquage
d3.select('body')
    .insert("input", '.paroles').attr('type', 'checkbox')
    .attr('class', 'checkbox')
    .attr('value', 'hideAll')
    .attr('id', 'hideAll');

d3.select('body')
    .insert("input", '.paroles').attr('type', 'checkbox')
    .attr('class', 'checkbox')
    .attr('value', 'hideRefrains')
    .attr('id', 'hideRefrains');

d3.select('body')
    .insert("label", '#hideAll')
    .attr('for', 'hideAll')
    .text('Hide All');

d3.select('body')
    .insert("label", '#hideRefrains')
    .attr('for', 'hideRefrains')
    .text('Hide Refrains');

d3.selectAll('label')
    .style('margin-left', '15px');

// HIDE ALL
d3.select('#hideAll')
    .on('click', function () {
        if (d3.select(this).property('checked')) {
            d3.select('.paroles').classed('hidden', true);
        } else {
            d3.select('.paroles').classed('hidden', false);
        }
    })

// HIDE REFRAINS
d3.select('#hideRefrains')
    .on('click', function () {
        if (d3.select(this).property('checked')) {
            d3.selectAll('.choeur').classed('hidden', true);
            d3.selectAll('.callback').classed('hidden', false);
            d3.selectAll('.callback')
                .on('mouseover', showRefrains)
                .on('mouseout', hideRefrains);
        } else {
            d3.selectAll('.choeur').classed('hidden', false);
            d3.selectAll('.callback').classed('hidden', true);
        }
    })



function showRefrains() {
    // NEXT SIBLING ELEMENT
    let next = d3.select(this).select(() => { return this.nextElementSibling });
    next.classed('hidden', false);
}

function hideRefrains() {
    let next = d3.select(this).select(() => { return this.nextElementSibling });
    next.classed('hidden', true);
}
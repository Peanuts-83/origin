
window.onload = function () {
    document.body.childNodes[1].innerHTML = "Rick Astley - Never Gonna Give You Up";

    let couplets = document.getElementsByClassName('couplet');
    for (let i=0; i<couplets.length; i++){
        couplets[i].firstChild.remove();
        couplets[i].firstChild.remove();
    }

    let refrains = document.getElementsByClassName('refrain');
    for (let i=0; i<refrains.length; i++){
        for (let j=0; j<refrains[i].childNodes.length; j += 2){
            refrains[i].childNodes[j].remove();
            refrains[i].childNodes[j].remove();
        }
    }

    erreur.remove();

    let footer = document.createElement('footer');
    footer.innerHTML = '© Copyright 2020 - Johnny H.'
    document.body.append(footer);
}

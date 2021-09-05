window.onload = function () {
    // remove red class
    let reds = document.getElementsByClassName('red');
    // convert HTML Collection to array with [...]
    [...reds].forEach(function (elem) {
        elem.classList.remove('red');
    });

    // add italic class
    let refrains = document.querySelectorAll('.refrain');
    [...refrains].forEach(function (elem) {
        elem.classList.add('italic');
    });

    // change blue color to #6495ED
    let blueColor = '#6495ED';
    document.body.classList.add('blue');
    document.getElementsByClassName('blue')[0].style.backgroundColor = blueColor;
}
// Récupere la case "masquer les paroles"
const checkboxParoles = document.querySelector('input#masquer-paroles');

// Récupère le div contenant les paroles
const divParoles = document.getElementById('paroles');

// Attache une fonction à l'évènement "click" sur checkboxParoles
checkboxParoles.addEventListener('click', function (event) {
  // event.target contient l'élément cliqué (ici checkboxParoles dans notre cas)
  if (event.target.checked) {
    divParoles.classList.add('hidden');
    checkboxParoles.nextElementSibling.innerHTML = 'Afficher les paroles';
  } else {
    divParoles.classList.remove('hidden');
    checkboxParoles.nextElementSibling.innerHTML = 'Masquer les paroles';
  }
});


const checkboxRefrains = document.getElementById('masquer-refrains');
const refrains = document.getElementsByClassName('contenu');
const refrainCallback = document.getElementsByClassName('definition');

checkboxRefrains.addEventListener('click', function (event) {
  if (event.target.checked) {
    [...refrains].forEach(function (elem) {
      elem.classList.add('hidden');
    });
    [...refrainCallback].forEach(function (elem) {
      elem.classList.remove('hidden');
      elem.addEventListener('mouseenter', function (event) {
        event.target.parentElement.querySelector('.contenu').classList.remove('hidden');
      });
      elem.addEventListener('mouseleave', function (event) {
        event.target.parentElement.querySelector('.contenu').classList.add('hidden');
      });

    })
  } else {
    [...refrains].forEach(function (elem) {
      elem.classList.remove('hidden');
    });
    [...refrainCallback].forEach(function (elem) {
      elem.classList.add('hidden');
    })

  }
});
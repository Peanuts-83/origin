src: <http://dartagnan.cg.helmo.be/~p150107/tutoriels/js-async/>

# Le contexte

Vous allez modéliser le concours télévisé "RockKids" permet à des métalleux en herbe de faire leurs preuves face à un jury composé de 4 stars du "Metal".

Chaque enfant effectue une prestation et se voit attribuer une cote sur 10 par arbitre (membre du jury). Son score final est l'addition des cotes du jury. L'enfant qui obtient le meilleur score remporte le concours.

Plusieurs gagnants sont possibles en cas d'égalité de points. Le ou les gagnants remportent le financement d'un album avec les 4 stars en featuring.

<br><br>

# La modélisation

### Le dépôt des scores obtenus est modélisé avec la classe DepotScores qui contient

```
    propriété "scores": dictionnaire de dictionnaires (clés 1ier niveau: les noms des arbitres, valeurs: dictionnaires (clés du 2ième niveau: les noms des enfants, valeurs: score)),
    méthode "sauverScore(arbitre, enfant, score)": ajoute le score attribué à un enfant par un arbitre,
    méthode "totaliserScores(enfant)": calcule le total des scores obtenus par un enfant
```

Créez ensuite une classe Enfant et une classe Arbitre qui héritent de la classe Personne:

```js
class Personne {
    constructor(nom){
        this.nom = nom;
    }
}
```

### La classe Arbitre implémente la méthode

```
    coter(depotScores, enfant): simule la cotation de la prestation d'un enfant par l'arbitre. L'arbitre peut coter (valeur aléatoire comprise entre [0 et 10]) dans un délai compris entre 0 et 5secondes maximum (utilisez setTimeout à cet effet).
```

### La classe Enfant implémente la méthode

```js
    obtenirScores(jury, scores): obtention du score de la part de chaque arbitre,
```

<br><br>

# 1. Exemple de programme à réaliser

```js
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

let scores = new DepotScores(jury);

enfants.forEach(e => e.obtenirScores(jury, scores));
```

<br><br>

# Résultat

```

Vote de Faro Lindemans sur Andréa Maxence ?

Vote de Dave Gilmort sur Andréa Maxence ?

Vote de Angus Old sur Andréa Maxence ?

Vote de Jacques Hetchamp sur Andréa Maxence ?

Vote de Faro Lindemans sur Ronan Vivien ?

Vote de Dave Gilmort sur Ronan Vivien ?

Vote de Angus Old sur Ronan Vivien ?

Vote de Jacques Hetchamp sur Ronan Vivien ?

Vote de Faro Lindemans sur Demetrio Yasmin ?

Vote de Dave Gilmort sur Demetrio Yasmin ?

Vote de Angus Old sur Demetrio Yasmin ?

Vote de Jacques Hetchamp sur Demetrio Yasmin ?

Vote de Faro Lindemans sur Kanya Lorenzo ?

Vote de Dave Gilmort sur Kanya Lorenzo ?

Vote de Angus Old sur Kanya Lorenzo ?

Vote de Jacques Hetchamp sur Kanya Lorenzo ?

Vote de Faro Lindemans sur Claptrap Jessica ?

Vote de Dave Gilmort sur Claptrap Jessica ?

Vote de Angus Old sur Claptrap Jessica ?

Vote de Jacques Hetchamp sur Claptrap Jessica ?

Vote de Faro Lindemans sur Sung Li ?

Vote de Dave Gilmort sur Sung Li ?

Vote de Angus Old sur Sung Li ?

Vote de Jacques Hetchamp sur Sung Li ?

Claptrap Jessica obtient 3 de la part de Dave Gilmort !

Claptrap Jessica obtient 3 de la part de Angus Old !

Claptrap Jessica obtient 6 de la part de Jacques Hetchamp !

Ronan Vivien obtient 9 de la part de Jacques Hetchamp !

Demetrio Yasmin obtient 4 de la part de Faro Lindemans !

Demetrio Yasmin obtient 5 de la part de Dave Gilmort !

Andréa Maxence obtient 7 de la part de Faro Lindemans !

Kanya Lorenzo obtient 6 de la part de Dave Gilmort !

Andréa Maxence obtient 8 de la part de Jacques Hetchamp !

Sung Li obtient 4 de la part de Angus Old !

Andréa Maxence obtient 8 de la part de Dave Gilmort !

Sung Li obtient 2 de la part de Jacques Hetchamp !

Andréa Maxence obtient 6 de la part de Angus Old !

Kanya Lorenzo obtient 1 de la part de Angus Old !

Demetrio Yasmin obtient 0 de la part de Angus Old !

Ronan Vivien obtient 2 de la part de Angus Old !

Claptrap Jessica obtient 8 de la part de Faro Lindemans !

Kanya Lorenzo obtient 5 de la part de Jacques Hetchamp !

Ronan Vivien obtient 6 de la part de Dave Gilmort !

Kanya Lorenzo obtient 9 de la part de Faro Lindemans !

Demetrio Yasmin obtient 4 de la part de Jacques Hetchamp !

Ronan Vivien obtient 5 de la part de Faro Lindemans !

Sung Li obtient 4 de la part de Dave Gilmort !

Sung Li obtient 4 de la part de Faro Lindemans !
```

<br>
<br>

# 2. Adaptez votre résolution de l'exercice précédent pour pouvoir afficher le score final obtenu par un enfant dès que tous les arbitres ont voté pour lui

Modifiez si nécessaire les signatures des méthodes..

```
Vote de Faro Lindemans sur Andréa Maxence ?

Vote de Dave Gilmort sur Andréa Maxence ?

Vote de Angus Old sur Andréa Maxence ?

Vote de Jacques Hetchamp sur Andréa Maxence ?

Vote de Faro Lindemans sur Ronan Vivien ?

Vote de Dave Gilmort sur Ronan Vivien ?

Vote de Angus Old sur Ronan Vivien ?

Vote de Jacques Hetchamp sur Ronan Vivien ?

Vote de Faro Lindemans sur Demetrio Yasmin ?

Vote de Dave Gilmort sur Demetrio Yasmin ?

Vote de Angus Old sur Demetrio Yasmin ?

Vote de Jacques Hetchamp sur Demetrio Yasmin ?

Vote de Faro Lindemans sur Kanya Lorenzo ?

Vote de Dave Gilmort sur Kanya Lorenzo ?

Vote de Angus Old sur Kanya Lorenzo ?

Vote de Jacques Hetchamp sur Kanya Lorenzo ?

Vote de Faro Lindemans sur Claptrap Jessica ?

Vote de Dave Gilmort sur Claptrap Jessica ?

Vote de Angus Old sur Claptrap Jessica ?

Vote de Jacques Hetchamp sur Claptrap Jessica ?

Vote de Faro Lindemans sur Sung Li ?

Vote de Dave Gilmort sur Sung Li ?

Vote de Angus Old sur Sung Li ?

Vote de Jacques Hetchamp sur Sung Li ?

Ronan Vivien obtient 3 de la part de Dave Gilmort !

Kanya Lorenzo obtient 3 de la part de Angus Old !

Kanya Lorenzo obtient 5 de la part de Dave Gilmort !

Andréa Maxence obtient 8 de la part de Dave Gilmort !

Sung Li obtient 1 de la part de Angus Old !

Ronan Vivien obtient 3 de la part de Faro Lindemans !

Claptrap Jessica obtient 1 de la part de Jacques Hetchamp !

Claptrap Jessica obtient 6 de la part de Faro Lindemans !

Demetrio Yasmin obtient 3 de la part de Jacques Hetchamp !

Claptrap Jessica obtient 7 de la part de Dave Gilmort !

Kanya Lorenzo obtient 2 de la part de Jacques Hetchamp !

Demetrio Yasmin obtient 9 de la part de Faro Lindemans !

Kanya Lorenzo obtient 9 de la part de Faro Lindemans !

***** Kanya Lorenzo obtient un total de 19 points. *****

Ronan Vivien obtient 10 de la part de Angus Old !

Andréa Maxence obtient 9 de la part de Angus Old !

Sung Li obtient 0 de la part de Jacques Hetchamp !

Demetrio Yasmin obtient 5 de la part de Dave Gilmort !

Sung Li obtient 5 de la part de Faro Lindemans !

Sung Li obtient 7 de la part de Dave Gilmort !

***** Sung Li obtient un total de 13 points. *****

Demetrio Yasmin obtient 3 de la part de Angus Old !

***** Demetrio Yasmin obtient un total de 20 points. *****

Andréa Maxence obtient 10 de la part de Faro Lindemans !

Ronan Vivien obtient 2 de la part de Jacques Hetchamp !

***** Ronan Vivien obtient un total de 18 points. *****

Claptrap Jessica obtient 6 de la part de Angus Old !

***** Claptrap Jessica obtient un total de 20 points. *****

Andréa Maxence obtient 6 de la part de Jacques Hetchamp !

***** Andréa Maxence obtient un total de 33 points. *****
```

<br>
<br>

# 3. Employez des Promises au lieu de callbacks

Commencez d'abord par réécrire votre résolution de l'exercice précédent à l'aide de promesses au lieu de callbacks, avant d'ajouter la contrainte suivante.

En réalité, il arrive que l'arbitre, pour faire le show, entame un "head-banging" au moment où on lui demande d'effectuer sa cotation et oublie de donner sa cote.

Pour simuler cela, créez une fonction  **interrogerArbitre()** qui retourne une promesse; cette fonction tire un temps de réponse aléatoire t compris entre [0 et 10] secondes:

* si ce temps est <= 5secondes, une valeur aléatoire entre [0, 10] est retournée après une attente de t secondes,
* sinon, cela veut dire que l'arbitre a épuisé son temps, une valeur aléatoire entre [5, 10] est retournée après 5 secondes d'attente au lieu de t secondes.

Encapsulez l'utilisation de "setTimeout" dans une promesse. Transformez le code pour exploiter les promesses au lieu de callbacks pour obtenir le total des scores d'un enfant dès que tous les arbitres ont voté.

*Affichez le ou les gagnants.*

```
Vote de Faro Lindemans sur Andréa Maxence ?

Vote de Dave Gilmort sur Andréa Maxence ?

Vote de Angus Old sur Andréa Maxence ?

Vote de Jacques Hetchamp sur Andréa Maxence ?

Vote de Faro Lindemans sur Ronan Vivien ?

Vote de Dave Gilmort sur Ronan Vivien ?

Vote de Angus Old sur Ronan Vivien ?

Vote de Jacques Hetchamp sur Ronan Vivien ?

Vote de Faro Lindemans sur Demetrio Yasmin ?

Vote de Dave Gilmort sur Demetrio Yasmin ?

Vote de Angus Old sur Demetrio Yasmin ?

Vote de Jacques Hetchamp sur Demetrio Yasmin ?

Vote de Faro Lindemans sur Kanya Lorenzo ?

Vote de Dave Gilmort sur Kanya Lorenzo ?

Vote de Angus Old sur Kanya Lorenzo ?

Vote de Jacques Hetchamp sur Kanya Lorenzo ?

Vote de Faro Lindemans sur Claptrap Jessica ?

Vote de Dave Gilmort sur Claptrap Jessica ?

Vote de Angus Old sur Claptrap Jessica ?

Vote de Jacques Hetchamp sur Claptrap Jessica ?

Vote de Faro Lindemans sur Sung Li ?

Vote de Dave Gilmort sur Sung Li ?

Vote de Angus Old sur Sung Li ?

Vote de Jacques Hetchamp sur Sung Li ?

Andréa Maxence obtient 6 de la part de Dave Gilmort !

Sung Li obtient 0 de la part de Dave Gilmort !

Ronan Vivien obtient 4 de la part de Angus Old !

Kanya Lorenzo obtient 6 de la part de Dave Gilmort !

Kanya Lorenzo obtient 6 de la part de Faro Lindemans !

Sung Li obtient 6 de la part de Angus Old !

Claptrap Jessica obtient 3 de la part de Jacques Hetchamp !

Sung Li obtient 9 de la part de Faro Lindemans !

Andréa Maxence obtient 9 de la part de Jacques Hetchamp !

Kanya Lorenzo obtient 2 de la part de Angus Old !

Demetrio Yasmin obtient 1 de la part de Faro Lindemans !

Ronan Vivien obtient 0 de la part de Faro Lindemans !

Claptrap Jessica obtient 8 de la part de Angus Old !

Andréa Maxence obtient 0 de la part de Faro Lindemans !

Arbitre Jacques Hetchamp distrait

Ronan Vivien obtient 6 de la part de Jacques Hetchamp !

Arbitre Dave Gilmort distrait

Demetrio Yasmin obtient 7 de la part de Dave Gilmort !

Arbitre Jacques Hetchamp distrait

Kanya Lorenzo obtient 6 de la part de Jacques Hetchamp !

***** Kanya Lorenzo obtient un total de 20 points. *****

Arbitre Dave Gilmort distrait

Claptrap Jessica obtient 6 de la part de Dave Gilmort !

Arbitre Faro Lindemans distrait

Claptrap Jessica obtient 9 de la part de Faro Lindemans !

***** Claptrap Jessica obtient un total de 26 points. *****

Arbitre Jacques Hetchamp distrait

Demetrio Yasmin obtient 8 de la part de Jacques Hetchamp !

Arbitre Jacques Hetchamp distrait

Sung Li obtient 7 de la part de Jacques Hetchamp !

***** Sung Li obtient un total de 22 points. *****

Arbitre Dave Gilmort distrait

Ronan Vivien obtient 6 de la part de Dave Gilmort !

***** Ronan Vivien obtient un total de 16 points. *****

Arbitre Angus Old distrait

Demetrio Yasmin obtient 8 de la part de Angus Old !

***** Demetrio Yasmin obtient un total de 24 points. *****

Arbitre Angus Old distrait

Andréa Maxence obtient 9 de la part de Angus Old !

***** Andréa Maxence obtient un total de 24 points. *****

Le(s) gagnant(s):

Claptrap Jessica gagne avec 26
```

<br>
<br>

# 4. Promise.all

Obligez à présent les arbitres à attendre que tous aient voté pour un enfant avant de passer à l'enfant suivant.

*Constatez le ralentissement notable de l'exécution... Dans vos scripts, ne forcez par les opérations asynchrones à être traitées comme synchrones si ce n'est pas nécessaire !*

```

Vote de Faro Lindemans sur Andréa Maxence ?

Vote de Dave Gilmort sur Andréa Maxence ?

Vote de Angus Old sur Andréa Maxence ?

Vote de Jacques Hetchamp sur Andréa Maxence ?

Andréa Maxence obtient 9 de la part de Angus Old !

Andréa Maxence obtient 0 de la part de Jacques Hetchamp !

Andréa Maxence obtient 2 de la part de Faro Lindemans !

Arbitre Dave Gilmort distrait

Andréa Maxence obtient 6 de la part de Dave Gilmort !

***** Andréa Maxence obtient un total de 17 points. *****

Vote de Faro Lindemans sur Ronan Vivien ?

Vote de Dave Gilmort sur Ronan Vivien ?

Vote de Angus Old sur Ronan Vivien ?

Vote de Jacques Hetchamp sur Ronan Vivien ?

Ronan Vivien obtient 9 de la part de Jacques Hetchamp !

Ronan Vivien obtient 0 de la part de Faro Lindemans !

Ronan Vivien obtient 1 de la part de Dave Gilmort !

Arbitre Angus Old distrait

Ronan Vivien obtient 6 de la part de Angus Old !

***** Ronan Vivien obtient un total de 16 points. *****

Vote de Faro Lindemans sur Demetrio Yasmin ?

Vote de Dave Gilmort sur Demetrio Yasmin ?

Vote de Angus Old sur Demetrio Yasmin ?

Vote de Jacques Hetchamp sur Demetrio Yasmin ?

Demetrio Yasmin obtient 2 de la part de Jacques Hetchamp !

Demetrio Yasmin obtient 6 de la part de Dave Gilmort !

Demetrio Yasmin obtient 9 de la part de Faro Lindemans !

Arbitre Angus Old distrait

Demetrio Yasmin obtient 5 de la part de Angus Old !

***** Demetrio Yasmin obtient un total de 22 points. *****

Vote de Faro Lindemans sur Kanya Lorenzo ?

Vote de Dave Gilmort sur Kanya Lorenzo ?

Vote de Angus Old sur Kanya Lorenzo ?

Vote de Jacques Hetchamp sur Kanya Lorenzo ?

Kanya Lorenzo obtient 9 de la part de Faro Lindemans !

Kanya Lorenzo obtient 1 de la part de Dave Gilmort !

Arbitre Angus Old distrait

Kanya Lorenzo obtient 7 de la part de Angus Old !

Arbitre Jacques Hetchamp distrait

Kanya Lorenzo obtient 9 de la part de Jacques Hetchamp !

***** Kanya Lorenzo obtient un total de 26 points. *****

Vote de Faro Lindemans sur Claptrap Jessica ?

Vote de Dave Gilmort sur Claptrap Jessica ?

Vote de Angus Old sur Claptrap Jessica ?

Vote de Jacques Hetchamp sur Claptrap Jessica ?

Claptrap Jessica obtient 5 de la part de Faro Lindemans !

Claptrap Jessica obtient 3 de la part de Dave Gilmort !

Claptrap Jessica obtient 8 de la part de Jacques Hetchamp !

Arbitre Angus Old distrait

Claptrap Jessica obtient 8 de la part de Angus Old !

***** Claptrap Jessica obtient un total de 24 points. *****

Vote de Faro Lindemans sur Sung Li ?

Vote de Dave Gilmort sur Sung Li ?

Vote de Angus Old sur Sung Li ?

Vote de Jacques Hetchamp sur Sung Li ?

Sung Li obtient 2 de la part de Faro Lindemans !

Sung Li obtient 0 de la part de Dave Gilmort !

Sung Li obtient 7 de la part de Jacques Hetchamp !

Sung Li obtient 0 de la part de Angus Old !

***** Sung Li obtient un total de 9 points. *****

Le(s) gagnant(s):

Kanya Lorenzo gagne avec 26
```

<br>
<br>

# 5. Version avec async/await

Adaptez votre résolution de l'exercice précédent avec des async/await au lieu de promesses.

*Constatez le ralentissement notable de l'exécution... Dans vos scripts, n'abusez pas des async/await pour des opérations asynchrones qui ne doivent pas être traitées comme synchrones !*
// 1. Clicking on the button the font, font size, and color of the paragraph text will be changed.
let txt = document.getElementById('text');
let x = 0;
function js_style(){
    if (x == 0){
        txt.innerHTML = "U clicked me!"
        txt.style.color = "red";
        txt.style.fontFamily = "Courrier"
        x++;
    } else if (x == 1) {
        txt.innerHTML = "JavaScript Exercises - w3resource"
        txt.style.color = "black";
        txt.style.fontFamily = "Times";
        x--;

    }
}

// 2. Write a JavaScript function to get the values of First and Last name of the following form.
// let result = document.getElementById("result");
function getFormValue(){
    event.preventDefault();
    console.log('fname by querySelector: ', document.querySelector("[name='fname']").value);
    console.log('fname by querySelectorAll: ', document.querySelectorAll("[type='text']")[0].value);
    console.log('fname by tagName: ', document.getElementsByTagName("input").fname.value);
    console.log('fname by id: ', document.getElementById('form1').fname.value);
    console.log('fname by name: ', document.getElementsByName('fname')[0].value);
    console.log('lname by name: ', document.getElementsByName('lname')[0].value);
}

// 3. Write a JavaScript program to set the background color of a paragraph.
function bg_color(){
    txt.style.background = 'red';
}

// 4. Here is a sample html file with a submit button. Write a JavaScript function to get the value of the href, hreflang, rel, target, and type attributes of the specified link.
let w3r = document.getElementById("w3r");
function getAttributes(){
    alert('href: ' + w3r.href);
    alert('hreflang: '+ w3r.hreflang);
    alert('rel: '+ w3r.rel);
    alert('target: '+ w3r.target);
    alert('type: '+ w3r.type);
}

// 5. Write a JavaScript function to add rows to a table.
let rowNum = 3;
function insert_Row(){
    let table = document.getElementById('sampleTable');
    let row = table.insertRow(rowNum-1);
    let cell1 = row.insertCell(0),
        cell2 = row.insertCell(1);
    cell1.innerHTML = `Row${rowNum} cell1`;
    cell2.innerHTML = `Row${rowNum} cell2`;
    rowNum++;
}

// 6. Write a JavaScript function that accept row, column, (to identify a particular cell) and a string to update the content of that cell.
function changeContent(){
    let table = document.getElementById('myTable');
    rowNum = window.prompt('Select row n°(0,1,2): ', 0);
    cellNum = window.prompt('Select cell n°(0,1): ', 0);
    str = window.prompt('Give message to print: ', 'default');
    table.rows[rowNum].cells[cellNum].innerHTML = str;
}

// 7. Write a JavaScript function that creates a table, accept row, column numbers from the user, and input row-column number as content (e.g. Row-0 Column-0) of a cell.
function createTable(){
    let table = document.getElementById('myTable');
    rowNum = window.prompt('Choose number of rows: ', 1);
    cellNum = window.prompt('Choose number of columns: ', 2);
    for (i=0; i<rowNum; i++){
        let row = table.insertRow(i);
        for (j=0; j<cellNum; j++){
            let cell = row.insertCell(j);
            cell.innerHTML = `Row ${i} cell ${j}`;
        }
    }
}

// 8. Write a JavaScript program to remove items from a dropdown list.
function removeColor(){
    let color = document.getElementById('colorSelect');
    color.remove(color.selectedIndex);
}

// 9. Write a JavaScript program to count and display the items of a dropdown list, in an alert window.
function getOptions(){
    let selector = document.getElementById('mySelect');
    let txt = `Selector has ${selector.length} options:`;
    for (color of selector){
        txt += '\n\t\t\t\t' + color.value;
    }
    alert(txt);
}

// 10. Write a JavaScript program to calculate the volume of a sphere.
function volumeSphere(){
    event.preventDefault();
    let radius = document.getElementById("radius").value;
    let volume = (4/3) * Math.PI * Math.pow(radius, 3);
    document.getElementById("volume").value =volume.toFixed(2);
}

// 11. Write a JavaScript program to display a random image (clicking on a button) from the following list.
function randomImg(){
    let img1 = {src: "http://farm4.staticflickr.com/3691/11268502654_f28f05966c_m.jpg", width: "240", height: "160"},
        img2 = {src: "http://farm1.staticflickr.com/33/45336904_1aef569b30_n.jpg", width: "320", height: "195"},
        img3 = {src: "http://farm6.staticflickr.com/5211/5384592886_80a512e2c9.jpg", width: "500", height: "343"};
    let arr = [img1, img2, img3];
    let choice = arr[Math.floor(Math.random() * 3)];
    let img = document.createElement("img");
    for (n in choice){
        img.setAttribute(n, img[n]);
    }
    alert(img.attributes)
    document.body.appendChild(img);
}

// 11b.Create constructor function Calculator that creates objetcs with 3 methods 
function Calculator() {
    this.read = function() {
        this.a = +prompt('a? ', 0);
        this.b = +prompt('b? ', 0);
    };
    this.sum = function() {
        return this.a + this.b;
    };
    this.mul = function() {
        return this.a * this.b;
    };
}
let calc = new Calculator();

// 11c.Create accumulator adding values and getting sum of all values accumulated.
function Accumulator() {
    this.counter = 0;
    this.read = function() {
        this.num = +prompt('num? ', 0);
        this.counter += this.num;
        document.getElementById('val').innerHTML += this.num + ' / ';
    };
    this.sum = function() {
        document.getElementById('sum').innerHTML = 'Sum = ' + this.counter;
        return this.counter;
    }
}
let acc = new Accumulator();

// 11d. Create a function readNumber which prompts for a number until the visitor enters a valid numeric value
function getNum(){
    let num = prompt('num?');
    while (!isFinite(num)) {
        num = prompt('num?');
    }
    (num === '' || num === null) ? alert('Aborted.') : alert('Number is ' + num);
}

/* 11e. Write the function sumInput() that:
Asks the user for values using prompt and stores the values in the array.
Finishes asking when the user enters a non-numeric value, an empty string, or presses
“Cancel”.
Calculates and returns the sum of array items.
P.S. A zero 0 is a valid number, please don’t stop the input on zero. */
function sumInput() {
    let num = +prompt('number? ');
    let arr = [num];
    while (isFinite(num) && num != NaN && num != '') {
        num = +prompt(`${arr} - Another number? `);
        arr.push(num);
    }
    let sum = 0;
    for (let n of arr) {sum += n};
    alert('Sum of values = '+ arr.join(' + ') + ' : ' + sum);
}
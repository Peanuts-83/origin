// 1/ Clicking on the button the font, font size, and color of the paragraph text will be changed.
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
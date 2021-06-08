function animate_string(id){
    let elt = document.getElementById(id);
    let txtNode = elt.childNodes[0];
    let txt = txtNode.data;

    setInterval(() => {
        txt = txt[1] + txt.substring(2) + txt[0];
        txtNode.data = txt;
    }, 100);
}
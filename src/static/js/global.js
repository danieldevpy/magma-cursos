const url = document.URL;

function setMenuSelected(){
    const urlSplit = url.split('/');
    const refine = urlSplit[3] + urlSplit[4];
    const p = document.getElementById(refine);
    p.className = p.className + " active";
    console.log(p.className);
}

window.addEventListener("load", function (event) {
  setMenuSelected();
});


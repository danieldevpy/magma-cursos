async function getPdf(pk){
    
    return fetch(`/certificate/make_pdf/${pk}`)
    .then(async response=>{
        return await response.blob()
    })

}

window.addEventListener("load", async function (event) {
    const pk = document.getElementById("labelPK");
    const response = await getPdf(pk.innerText);
    const urlPdf = URL.createObjectURL(response);
    const iframePdf = document.getElementById("iframe");
    iframePdf.src = urlPdf;
    iframePdf.style = `width: ${width}px; height: ${width}px;`
});


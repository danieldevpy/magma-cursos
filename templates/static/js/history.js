const generates = {}

var width = 600

async function getPdf(pk){
    
    return fetch(`/certificate/make_pdf/${pk}`)
    .then(async response=>{
        return await response.blob()
    })

}


function showDiv(elemnt){

}

async function RenderCertificate(pk, show){
    console.log(show);
    const id = pk.split(' ')[1]
    const divCertificate = document.getElementById(pk);
    const divChild = document.getElementById(pk+" child");

    if(pk in generates){

        if(show){
            divChild.style.display = "none";
            const iframePdf = generates[pk]['iframe']
            iframePdf.style.display = "block";
            const button_back = generates[pk]['button_back']
            button_back.style.display = "block";
        }else{
      
            divChild.style.display = "block";
            const iframePdf = generates[pk]['iframe']
            iframePdf.style.display = "none";
            const button_back = generates[pk]['button_back']
            button_back.style.display = "none";
        }


    }else{
  
        divChild.style.display = "none";
        const spinner = document.createElement('div');
        spinner.className = "spinner-border"
        spinner.style.alignSelf = "center";
        divCertificate.appendChild(spinner);
        const response = await getPdf(id);
        const urlPdf = URL.createObjectURL(response);
        const iframePdf = document.createElement("iframe");
        iframePdf.src = urlPdf;
        iframePdf.style = `width: ${width}px; height: ${width}px;`
        divCertificate.appendChild(iframePdf);
                
        const button_back = document.createElement("button");
        button_back.innerText = "Fechar"
        button_back.className = "btn btn-danger";
        button_back.style.margin = "5px";
        button_back.onclick = function() {
            RenderCertificate(pk, false);
        };
        

        divCertificate.appendChild(button_back);
        
        spinner.style.display = "none";
        generates[pk] = {'button_back': button_back, 'iframe': iframePdf};
    }

}

function SearchResponse(){
    const input = document.getElementById("inputSearch");
    const value = input.value;
    if(!value) return;

    window.location.href = `/dash/history/${value}`;
}





window.addEventListener("load", function (event) {
    var windowSize = window.innerWidth;
    if(windowSize < 800){
        width = window.innerWidth - 100;
    }
   

    document.getElementById("inputSearch").addEventListener("keydown", function(event) {
        // Verifique se a tecla pressionada é a tecla Enter (código 13)
        if (event.keyCode === 13) {
            // Chame a função desejada aqui
            SearchResponse();
        }
    });
});


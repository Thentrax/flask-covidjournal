function filtraNoticia(estado) {
    var seletor = document.querySelectorAll(estado);
    var cards = document.querySelectorAll('.card');
    
    cards.forEach(element => {
        element.style.display="none";
    });



    if (seletor.length == 0) {
        var msg = document.querySelector('#msg')
        msg.innerHTML = "<p class='text-center m-2'>Sem notícias desse estado...</p>";
    }
    else{
        seletor.forEach(element => {
            element.style.display="flex";
        });

        var msg = document.querySelector('#msg')
        msg.innerHTML = "";

    }

}

function mostrarTodas() {
    var cards = document.querySelectorAll('.card');
    var msg = document.querySelector('#msg')
    msg.innerHTML = "";

    cards.forEach(element => {
        element.style.display="flex";
    });

}
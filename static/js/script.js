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

function pesquisarNoticia() {
    var input = document.getElementById("search").value;
    input= input.toLowerCase();
    var cards = document.getElementsByClassName('card');
    var title = document.getElementsByClassName('card-title');
    var text = document.getElementsByClassName('card-text');

    var msg = document.querySelector('#msg')
    msg.innerHTML = "";
    
    for (i = 0; i < cards.length; i++) {

        if (!title[i].innerHTML.toLowerCase().includes(input) && (!text[i].innerHTML.toLowerCase().includes(input))) {
            cards[i].style.display="none";
        }
        else{
            cards[i].style.display="flex";
            console.log(i, text[i])

        }
    }
}
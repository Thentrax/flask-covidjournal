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
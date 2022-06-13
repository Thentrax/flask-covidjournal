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

{
    var form = document.querySelector(".form_comentario");
    function abrirFormulario() {
        form.innerHTML = `
        <div class="form-group">
        <div class="form-flex">
            <div class="item-form-flex">
                <label for="author">Nome:</label>
                <input type="text" class="form-control form-name" id="author" name="author" placeholder="Nome">
            </div>
            <div class="item-form-flex form-like">
                <label for="like">Gostou da Notícia?</label>
                <br>
                <input type="checkbox" name="like" id="like" class="like-box">
            </div>
        </div>
    <div class="form-group">
            <label for="text">Comentário:</label>
            <textarea class="form-control" id="text" name="text" rows="3"></textarea>
    </div>
    <div class="row">
        <div class="col">
            <button type="submit" class="btn btn-primary add-coment">Enviar</button>
            <button class="btn btn-primary add-coment" onclick="fecharFormulario()"> Cancelar</button>
        </div>
    </div>`;
    }

    function fecharFormulario() {
        form.innerHTML = '';
    }
}

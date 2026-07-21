const form = document.getElementById("questionForm");

const input = document.getElementById("pregunta");

const chat = document.getElementById("chat");

const thinking = document.getElementById("thinking");

input.focus();

form.addEventListener("submit", function(){

    if(thinking){
        thinking.style.display = "block";
    }

    const loading = document.createElement("div");

    loading.className = "assistant loading";

    loading.innerHTML = "<strong>Pegasus</strong><p>⏳ Pensando...</p>";

    chat.appendChild(loading);

    chat.scrollTop = chat.scrollHeight;

});

input.addEventListener("keypress", function(event){

    if(event.key === "Enter"){

        event.preventDefault();

        form.submit();

    }

});
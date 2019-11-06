


function html_elements(response) {
    var responses = document.querySelector("#responses");
    response = document.createElement("div");
    response.classList.add("response");
    responses.appendChild(response);

    var response = document.querySelector(".response");
    p = document.createElement("p");
    p.classList.add("grandpy-answer");
    p.textContent = 
    div = document.createElement("div");
    div.classList.add("map");
    article = document.createElement("article");
    article.classList.add("wikipedia_article");
    article.textContent = data.info['extract'];
    response.appendChild(p);
    response.appendChild(div);
    response.appendChild(article);

    var article = document.querySelector(".wikipedia_article");
    a = document.createElement("a");
    a.href = info['fullurl'];
    a.textContent = "En savoir plus";
    article.appendChild(a);
}

var form = document.querySelector("form");
form.addEventListener("submit", function (e) {
    e.preventDefault();
    var data = new FormData(form);
    ajaxPost(localhost/api, data, function (response) {
        var data = JSON.parse(reponse);
        html_elements(data);
    });
});

var responses = document.querySelector("#responses");
response = document.createElement("div");
response.classList.add("response");
responses.appendChild(response);

var response = document.querySelector(".response");
p = document.createElement("p");
p.classList.add("grandpy-answer");
div = document.createElement("div");
div.classList.add("map");
article = document.createElement("article");
article.classList.add("wikipedia_article");
article.textContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
;
response.appendChild(p);
response.appendChild(div);
response.appendChild(article);

var article = document.querySelector(".wikipedia_article");
a = document.createElement("a");
a.href = "https://openclassrooms.com";
a.textContent = "En savoir plus";
article.appendChild(a);


form.addEventListener("submit", function (e) {
    var pseudo = form.elements.input.value;
    // if (form.elements.confirmation.checked) {

    // } else {

});

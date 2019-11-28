/**
 * create a response to a question sent to grangpy
 */
function htmlElements(responseText) {
    document.body.style.cursor = "default";
    
    // create a response container
    var data = JSON.parse(responseText);
    var responses = document.querySelector("#responses");
    var response = document.createElement("div");
    response.classList.add("response");
    responses.appendChild(response);

    // create a response
    response = document.querySelector(".response");
    p = document.createElement("p");
    p.classList.add("grandpy-answer");
    p.textContent = data["grandpy_answer"] + data["address"];
    response.appendChild(p);

    // create a response google map and marker
    var map = document.createElement("div");
    map.classList.add("map");
    var mapObject = new google.maps.Map(map, {
        center: {
            lat: data["lat"], 
            lng: data["lng"]
        },
        zoom: 8
    });
    var markerObject = new google.maps.Marker({
        position: {
            lat: data["lat"],
            lng: data["lng"]
        }, 
        map: mapObject}
    );
    response.appendChild(map);
    
    // create a response google map and marker
    article = document.createElement("article");
    article.classList.add("wikipedia_article");
    if (data["error"] == false) {
        p.textContent = data["grandpy_answer2"] + data['extract'];
    }
    response.appendChild(article);

    // create a response link to wikipedia article
    a = document.createElement("a");
    a.href = data['fullurl'];
    a.textContent = "En savoir plus";
    article.appendChild(a);

    // scrolling to last grandpy response
    response.scrollIntoView();
}

var form = document.querySelector("form");
form.addEventListener("submit", function (e) {
    e.preventDefault();
    var data = new FormData(form);
    ajaxPost("/api", data, htmlElements);
    document.body.style.cursor = "wait";
});

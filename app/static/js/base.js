/**
 * create a response to a question sent to grangpy
 */
function htmlElements(responseText) {
    document.body.style.cursor = "default";
    
    // create a response container
    let data = JSON.parse(responseText);
    let responses = document.querySelector("#responses");
    let response = document.createElement("div");
    response.classList.add("response");
    responses.appendChild(response);

    // create a response
    let answer = document.querySelector(".response");
    let p = document.createElement("p");
    p.classList.add("grandpy-answer");
    p.textContent = data["grandpy_answer"] + data["address"];
    answer.appendChild(p);

    // create a response google map and marker
    let map = document.createElement("div");
    map.classList.add("map");
    let mapObject = new google.maps.Map(map, {
        center: {
            lat: data["lat"], 
            lng: data["lng"]
        },
        zoom: 8
    });
    let markerObject = new google.maps.Marker({
        position: {
            lat: data["lat"],
            lng: data["lng"]
        }, 
        map: mapObject}
    );
    response.appendChild(map);
    
    // create a response google map and marker
    let article = document.createElement("article");
    article.classList.add("wikipedia_article");
    if (data["error"] == false) {
        article.textContent = data["grandpy_answer2"] + data['extract'] + "  ... ZZZZZzzzz  Il s'est endormi. Profitez en pour ";
    }
    response.appendChild(article);

    // create a response link to wikipedia article
    let a = document.createElement("a");
    a.href = data['fullurl'];
    a.textContent = "en savoir plus ici.";
    article.appendChild(a);

    // scrolling to last grandpy response
    response.scrollIntoView();
}

let form = document.querySelector("form");
form.addEventListener("submit", function (e) {
    e.preventDefault();
    let data = new FormData(form);
    ajaxPost("/api", data, htmlElements);
    document.body.style.cursor = "wait";
});

function search() {
    phrase = document.getElementById("q").value;
    get_search(phrase);
}

function get_search(phrase) {
        $.get("/search", {q: phrase}, changeData);
}

function changeData(data) {
    var element = $("#content");
    $("#content").html(data);
}
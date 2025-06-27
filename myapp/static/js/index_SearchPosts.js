function searchPosts() {
    var searchInput = document.getElementById("searchButton").value.toLowerCase();
    var articles = document.getElementsByTagName("article");
    for (var i = 0; i < articles.length; i++) {
        var title = articles[i].getElementsByClassName("article-title")[0].innerText.toLowerCase();
        if (title.includes(searchInput)) {
            articles[i].style.display = "block";
        } else {
            articles[i].style.display = "none";
        }
    }
}
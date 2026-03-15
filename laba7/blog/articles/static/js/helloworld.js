var foldBtns = document.getElementsByClassName('fold-button');

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function (e) {
        var button = e.target;
        var post = button.parentElement;

        if (post.classList.contains("folded")) {
            post.classList.remove("folded");
            button.innerHTML = "свернуть";
        } else {
            post.classList.add("folded");
            button.innerHTML = "развернуть";
        }
    });
}

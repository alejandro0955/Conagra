

function add_suggestion(text) {
    div = document.createElement("div");
    div.id = "suggestion";
    height = document.getElementById("suggestions").offsetHeight
    div.innerHTML = text
    // div.style.height = String(height/5)+"px";
    document.getElementById("suggestions").appendChild(div);
}

function add_item(text) {
    a = document.createElement("button");
    a.id = "item";
    a.innerHTML = text
    a.onclick = function () {
        this.style.display = "none";
    }
    document.getElementById("product_line").appendChild(a);

}

function add_items(vars) {
    for (let i = 0; i < vars.length; i++) {
        add_item(vars[i]);
      }
}

function pass(vars) {
    add_suggestion(vars.suggestion1)
    add_suggestion(vars.suggestion2)
    add_suggestion(vars.suggestion3)
    add_suggestion(vars.suggestion4)
    add_suggestion(vars.suggestion5)
    
}




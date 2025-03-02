// Opens external links in a new tab with security attributes
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a[href]").forEach((link) => {
        if (link.hostname !== window.location.hostname) {
            link.setAttribute("target", "_blank");
            link.setAttribute("rel", "noopener noreferrer");
        }
    });
});

// © Copyright year. Last updated on Month date, year.
document.addEventListener("DOMContentLoaded", function () {
    let today = new Date();
    let year = today.getFullYear();
    let formattedDate = today.toLocaleDateString('en-US', {
        year: 'numeric', month: 'short', day: 'numeric'
    });

    let copyrightText = `<p>© Copyright ${year}. Last updated on ${formattedDate}.</p>`;

    // Select the <div role="contentinfo"> where the copyright should appear before
    let contentInfo = document.querySelector("footer div[role='contentinfo']");

    if (contentInfo) {
        // Insert copyright before the content info div
        contentInfo.insertAdjacentHTML("beforebegin", copyrightText);
    }
});


//Styling file name in a webpage
const file_title_elem = document.querySelectorAll(".doc.doc-object.doc-module");
for(var i = 0; i < file_title_elem.length; i++){
    file_title_elem[i].querySelector("h2").querySelector("code").style.color = "black";
    file_title_elem[i].querySelector("h2").querySelector("code").style.border = "none";
}


//Appending "class" before the class names
const class_elems = document.querySelectorAll(".doc.doc-object.doc-class");
for(var i = 0; i < class_elems.length; i++){
    const code_elem = class_elems[i].querySelector("h3").querySelector("code");
    code_elem.innerHTML = "<span class='class'>class </span>" + code_elem.innerHTML;
}

//Styling of classes headers
for(var i = 0; i < class_elems.length; i++){
    const code_elem = class_elems[i].querySelector("h3").querySelector("code");
    const keyword_class = code_elem.querySelector(".class");
    keyword_class.style.color = "#2980b9";  //class keyword colored to blue

    //change the colors of class parameters to blue
    const n = code_elem.querySelectorAll(".n");
    for(var j = 0; j < n.length; j++){
        if(j != 0){ //except the first occurence which is the class name
            n[j].style.color = "#2980b9";
        }
    }
    const o = code_elem.querySelectorAll(".o");
    for(var j = 0; j < o.length; j++){
        o[j].style.color = "#2980b9";
    }
    const p = code_elem.querySelectorAll(".p");
    for(var j = 0; j < p.length; j++){
        p[j].style.color = "#2980b9";
    }
    const kc = code_elem.querySelectorAll(".kc");
    for(var j = 0; j < kc.length; j++){
        kc[j].style.color = "#2980b9";
    }

    //change class name color to black
    if(p.length != 0){
        n[0].style.color = "#000";
    }
    else{
        code_elem.style.color = "#000";
    }
    //set background and top border
    code_elem.style.border = "none";
    const h3 = class_elems[i].querySelector("h3");
    h3.style.borderTop = "3px solid #6ab0de";
    h3.style.background = "#e7f2fa";
    code_elem.style.background = "#e7f2fa";
    h3.style.width = "fit-content";
    h3.style.paddingRight = "3px";
}

//styling of class contents
for(var j = 0; j < class_elems.length; j++){
    const attributes = class_elems[j].querySelectorAll(".doc.doc-object.doc-attribute");
    for(var i = 0; i < attributes.length; i++){
        //class attributes box styling
        attributes[i].style.background = "#f0f0f0";
        attributes[i].style.borderLeft = "3px solid #ccc";
        attributes[i].style.width = "fit-content";

        //class attribute name styling
        const code = attributes[i].querySelector("code")
        code.style.background = "#f0f0f0";
        code.style.border = "none";
        code.style.color = "black";

        //set color to grey to the elements after the class attribute name
        const span = code.querySelectorAll("span");
        for(var k = 1; k < span.length; k++){
            span[k].style.color = "#555";
        }

        //REMOVING THE "class-attribute", "instance-attribute"
        const small = attributes[i].querySelectorAll("small");
        for(var k = 0; k < small.length; k++){
            small[k].style.display = "none";
        }
    }
}




// styling the function headers
const func = document.querySelectorAll(".doc.doc-object.doc-function");
for(var i = 0; i < func.length; i++){
    const code = func[i].querySelector("code");
    code.style.background = "#e7f2fa";
    code.style.border = "none";
    code.querySelector(".n").style.color = "#000";
    const spans = code.querySelectorAll("span");
    for(var j = 1; j < spans.length; j++){
        spans[j].style.color = "#2980b9";
    }

    const header = func[i].querySelector("h3, h4");
    if(header){
        header.style.background = "#e7f2fa";
        header.style.borderTop = "3px solid #6ab0de";
        header.style.width = "fit-content";
    }
}

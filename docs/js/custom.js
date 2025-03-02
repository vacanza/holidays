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


document.addEventListener("DOMContentLoaded", () => {
    // Style File Name in the Webpage
    document.querySelectorAll(".doc.doc-object.doc-module").forEach(module => {
        const codeElem = module.querySelector("h2 code");
        if (codeElem) {
            codeElem.style.color = "black";
            codeElem.style.border = "none";
        }
    });

    // Append "class" Before Class Names
    document.querySelectorAll(".doc.doc-object.doc-class").forEach(classElem => {
        const codeElem = classElem.querySelector("h3 code");
        if (codeElem) {
            codeElem.innerHTML = "<span class='class'>class </span>" + codeElem.innerHTML;
        }
    });

    // Style Class Headers
    document.querySelectorAll(".doc.doc-object.doc-class").forEach(classElem => {
        const codeElem = classElem.querySelector("h3 code");
        if (!codeElem) return;

        // Style "class" keyword
        const classKeyword = codeElem.querySelector(".class");
        if (classKeyword) classKeyword.style.color = "#2980b9";

        // Style parameters inside class definition
        ["n", "o", "p", "kc"].forEach(cls => {
            codeElem.querySelectorAll(`.${cls}`).forEach((elem, index) => {
                if (cls === "n" && index === 0) return; // Skip first occurrence (class name)
                elem.style.color = "#2980b9";
            });
        });

        // Ensure class name is black
        const firstParam = codeElem.querySelector(".p");
        if (firstParam) {
            const firstN = codeElem.querySelector(".n");
            if (firstN) firstN.style.color = "#000";
        } else {
            codeElem.style.color = "#000";
        }

        // Set background and border styles for class headers
        const h3Elem = classElem.querySelector("h3");
        if (h3Elem) {
            h3Elem.style.borderTop = "3px solid #6ab0de";
            h3Elem.style.background = "#e7f2fa";
            h3Elem.style.width = "fit-content";
            h3Elem.style.paddingRight = "3px";
        }
        codeElem.style.background = "#e7f2fa";
        codeElem.style.border = "none";
    });

    // Style Class Contents
    document.querySelectorAll(".doc.doc-object.doc-class").forEach(classElem => {
        classElem.querySelectorAll(".doc.doc-object.doc-attribute").forEach(attribute => {
            // Box styling for attributes
            attribute.style.background = "#f0f0f0";
            attribute.style.borderLeft = "3px solid #ccc";
            attribute.style.width = "fit-content";

            // Class attribute name styling
            const code = attribute.querySelector("code");
            if (code) {
                code.style.background = "#f0f0f0";
                code.style.border = "none";
                code.style.color = "black";

                // Set elements after class attribute name to grey
                code.querySelectorAll("span").forEach((span, index) => {
                    if (index > 0) span.style.color = "#555";
                });
            }

            // Remove "class-attribute", "instance-attribute" labels
            attribute.querySelectorAll("small").forEach(small => {
                small.style.display = "none";
            });
        });
    });

    // Style Function Headers
    document.querySelectorAll(".doc.doc-object.doc-function").forEach(funcElem => {
        const code = funcElem.querySelector("code");
        if (!code) return;

        code.style.background = "#e7f2fa";
        code.style.border = "none";

        // Style function name (first `.n` should be black)
        const functionName = code.querySelector(".n");
        if (functionName) functionName.style.color = "#000";

        // Style function parameters
        code.querySelectorAll("span").forEach((span, index) => {
            if (index > 0) span.style.color = "#2980b9";
        });

        // Apply styles to `h3` or `h4` headers inside function blocks
        const header = funcElem.querySelector("h3, h4");
        if (header) {
            header.style.background = "#e7f2fa";
            header.style.borderTop = "3px solid #6ab0de";
            header.style.width = "fit-content";
        }
    });
});

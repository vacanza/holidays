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

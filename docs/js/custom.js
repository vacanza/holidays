document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a[href]").forEach((link) => {
        if (link.hostname !== window.location.hostname) {
            link.setAttribute("target", "_blank");
            link.setAttribute("rel", "noopener noreferrer");
        }
    });
});

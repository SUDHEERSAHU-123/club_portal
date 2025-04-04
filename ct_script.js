function showSection(sectionId) { 
    // Hide all sections first
    let allSections = document.querySelectorAll(".members");
    allSections.forEach(section => {
        section.classList.remove("show");
    });

    // Show only the selected section
    document.getElementById(sectionId).classList.add("show");
}

document.addEventListener("DOMContentLoaded", function () {
    let members = document.querySelectorAll(".rotation-container");

    members.forEach((member) => {
        const backImage = member.querySelector(".back-image");
        const frontImage = member.querySelector(".front-image");
        const link = member.querySelector("a");

        // Show front image on hover
        member.addEventListener("mouseenter", function() {
            backImage.style.opacity = "0";
            frontImage.style.display = "block";
            frontImage.style.opacity = "1";
        });

        // Show back image when hover ends
        member.addEventListener("mouseleave", function() {
            backImage.style.opacity = "1";
            frontImage.style.opacity = "0";
            setTimeout(() => {
                frontImage.style.display = "none";
            }, 300); // Match this with CSS transition duration
        });

        // Handle click for LinkedIn redirect
        member.addEventListener("click", function() {
            if (link) {
                window.open(link.href, "_blank");
            }
        });
    });
});
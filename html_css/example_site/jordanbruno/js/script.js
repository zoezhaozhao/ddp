console.log("Hello DDP Class!!!");

document.addEventListener('DOMContentLoaded', function () {
    const profilePic = document.querySelector("#profile img");

    profilePic.addEventListener("mouseover", function () {
        this.src = "images/profile-hover.png";
    });

    profilePic.addEventListener("mouseout", function () {
        this.src = "images/profile.png";
    });
});

let userControls = document.querySelector('.userDropdown__content');
let userControlsActionBtn = document.querySelector('.userDropdown__actionBlock');

window.addEventListener('click', () => {
    userControls.style.display = "none";
})

userControlsActionBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    toggleUserControls();
})

const toggleUserControls = () => {
    userControls.style.display = (['','none'].includes(userControls.style.display)) ? 'block' : 'none';
}
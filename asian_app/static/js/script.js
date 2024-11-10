function burgerMenuAction() {
    const menuList = document.getElementById('menu-list');
    if (menuList.style.display === 'none' || menuList.style.display === '') {
        menuList.style.display = 'block';
    } else {
        menuList.style.display = 'none';
    }
}
window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});

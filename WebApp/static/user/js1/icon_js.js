function toggleUserMenu() {
    const menu = document.getElementById('user-menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

function logout() {
    // Perform logout operations here
    alert("Logging out from this account....");
    toggleUserMenu();
}

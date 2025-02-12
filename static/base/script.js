(function() {
    const handleLogoutMenu = () => {
        const btn_open_logout = document.querySelector('#btn-open-menu-logout');
        const menu_logout = document.querySelector('#menu-logout');

        btn_open_logout.addEventListener('click', function(event) {
            event.stopPropagation();
            menu_logout.classList.toggle('visible');
        });

        document.addEventListener('click', function(event) {
            if (!menu_logout.contains(event.target) && !btn_open_logout.contains(event.target)) {
                menu_logout.classList.remove('visible');
            }
        });
    }

    document.addEventListener('DOMContentLoaded', function() {
        handleLogoutMenu();
    });
})();
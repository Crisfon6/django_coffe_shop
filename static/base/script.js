(function() {
    const start = () => {
        handleLogoutMenu();
    }

    const handleLogoutMenu = () => {
        let btnOpenMenuLogout = document.getElementById('btn-open-menu-logout');
        let menu_logout = document.getElementById('menu-logout');

        // Toggle menu when clicking the button
        btnOpenMenuLogout.addEventListener('click', function(e) {
            e.stopPropagation(); // Prevent click from bubbling to document
            if (menu_logout.style.display === 'none') {
                menu_logout.style.display = 'block';
            } else {
                menu_logout.style.display = 'none';
            }
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            // Check if click is outside both the button and menu
            if (!btnOpenMenuLogout.contains(e.target) && !menu_logout.contains(e.target)) {
                menu_logout.style.display = 'none';
            }
        });

        // Prevent menu from closing when clicking inside it
        menu_logout.addEventListener('click', function(e) {
            e.stopPropagation(); // Prevent click from bubbling to document
        });
    }

    document.addEventListener('DOMContentLoaded', function() {
        start();
    });
})();
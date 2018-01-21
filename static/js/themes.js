THEME_COOKIE_KEY = "theme"
PRIMARY_COOKIE_KEY = "primary"
SECONDARY_COOKIE_KEY = "secondary"


function changeTheme(theme, primary, secondary) {
    $(".gk-theme-text").css(
        "color", primary
    );
    $(".gk-theme-text").css(
        "text-shadow", "2px 2px " + secondary
    );
    createCookie(THEME_COOKIE_KEY, theme);
    createCookie(PRIMARY_COOKIE_KEY, primary);
    createCookie(SECONDARY_COOKIE_KEY, secondary);
}


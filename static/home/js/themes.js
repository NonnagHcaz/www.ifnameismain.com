THEME_COOKIE_KEY = "theme"
PRIMARY_COOKIE_KEY = "primary"
SECONDARY_COOKIE_KEY = "secondary"


function changeTheme(theme, primary, secondary) {
    var age = 7
    $(".gk-theme-text").css(
        "color", primary
    );
    $(".gk-theme-text").css(
        "text-shadow", "2px 2px " + secondary
    );
    eraseCookie(PRIMARY_COOKIE_KEY);
    eraseCookie(SECONDARY_COOKIE_KEY);
    createCookie(PRIMARY_COOKIE_KEY, primary, age);
    createCookie(SECONDARY_COOKIE_KEY, secondary, age);
}


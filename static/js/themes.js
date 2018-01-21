THEME_COOKIE_KEY = "theme"
PRIMARY_COOKIE_KEY = "primary"
SECONDARY_COOKIE_KEY = "secondary"
THEME_BASEDIR = "css/gkit_css/themes/"
THEME_FILE = "/theme.css"

function changeTheme(theme, primary, secondary, json_path, static_path) {
    $(".gk-theme-text-element").css(
        "color", primary
    );
    $(".gk-theme-text-element").css(
        "text-shadow", "2px 2px " + secondary
    );
    createCookie(THEME_COOKIE_KEY, theme);
    createCookie(PRIMARY_COOKIE_KEY, primary);
    createCookie(SECONDARY_COOKIE_KEY, secondary);
    loadThemes(json_path, static_path);
}

function getSheetName(theme, static_path) {
    return (static_path + THEME_BASEDIR + theme + THEME_FILE);
}

function loadThemes(json_path, static_path) {
    var curr_theme = readCookie(THEME_COOKIE_KEY);

    $(".theme-dropdown-item").remove();
    $.getJSON(json_path, function(data) {
        $.each(data, function(index, element) {
            if (curr_theme && element.id == curr_theme) {
                is_selected = " w3-grey";
            } else {
                is_selected = "";
            }
            $("#theme-dropdown-top-items").append(
              $("<a>", {
                href: "javascript:void(0);",
                onclick: "changeTheme('" + element.id + "', '" + element.primary + "', '" + element.secondary + "', '" + json_path +"', '" + static_path + "');",
                class: "w3-bar-item w3-button theme-dropdown-item" + is_selected,
                text: element.name
              })
            );
            $("#theme-dropdown-side-items").append(
                $("<a>", {
                href: "javascript:void(0);",
                onclick: "changeTheme('" + element.id + "', '" + element.primary + "', '" + element.secondary + "', '" + json_path +"', '" + static_path + "');",
                class: "w3-bar-item w3-button theme-dropdown-item" + is_selected,
                text: element.name
            }));
        });});
}

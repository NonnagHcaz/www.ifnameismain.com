THEME_COOKIE_KEY = "theme"
THEME_BASEDIR = "/static/css/gkit_css/themes/"
THEME_HEAD = "gk_theme_"

function changeTheme(theme) {
    newstylesheet = getSheetName(theme);

    if ($("#dynamic_css").length == 0) {
        $("head").append("<link>")
        css = $("head").children(":last");

        css.attr({
          id: "dynamic_css",
          rel:  "stylesheet",
          type: "text/css",
          href: newstylesheet
        });
    } else {
        $("#dynamic_css").attr("href",newstylesheet);
    }
    eraseCookie(THEME_COOKIE_KEY);
    createCookie(THEME_COOKIE_KEY, theme, 1);
}

function getSheetName(theme) {
    return (THEME_BASEDIR + THEME_HEAD + theme + ".css");
}

function loadThemes(json_path, static_path) {
    $.getJSON(json_path, function(data) {
        $.each(data, function(index, element) {
            $("#theme-dropdown-items").append(
                $("<a>", {
                    href: "javascript:void(0);",
                    onclick: "changeTheme('" + element.key + "');",
                    class: "w3-bar-item w3-button",
                    text: element.canonical
                }));});});
}

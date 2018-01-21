THEME_COOKIE_KEY = "theme"
THEME_BASEDIR = "css/gkit_css/themes/"
THEME_FILE = "/theme.css"

function changeTheme(theme, json_path, static_path) {
    newstylesheet = getSheetName(theme, static_path);

    // if ($("#dynamic_css").length == 0) {
    //     $("head").append("<link>")
    //     css = $("head").children(":last");

    //     css.attr({
    //       id: "dynamic_css",
    //       rel:  "stylesheet",
    //       type: "text/css",
    //       href: newstylesheet
    //     });
    // } else {
    //     $("#dynamic_css").attr("href",newstylesheet);
    // }
    eraseCookie(THEME_COOKIE_KEY);
    createCookie(THEME_COOKIE_KEY, theme);
    loadThemes(json_path, static_path);
}

function getSheetName(theme, static_path) {
    return (static_path + THEME_BASEDIR + theme + THEME_FILE);
}

function loadThemes(json_path, static_path) {
    var curr_theme = readCookie(THEME_COOKIE_KEY);
    // $("#theme-dropdown-top-items").empty();
    // $("#theme-dropdown-side-items").empty();
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
                onclick: "changeTheme('" + element.id + "', '" + json_path +"', '" + static_path + "');",
                class: "w3-bar-item w3-button theme-dropdown-item" + is_selected,
                text: element.name
              })
            );
            $("#theme-dropdown-side-items").append(
                $("<a>", {
                href: "javascript:void(0);",
                onclick: "changeTheme('" + element.id + "', '" + json_path +"', '" + static_path + "');",
                class: "w3-bar-item w3-button theme-dropdown-item" + is_selected,
                text: element.name
            }));
        });});
}

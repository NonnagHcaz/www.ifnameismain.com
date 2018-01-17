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
    eraseCookie("theme");
    createCookie("theme", theme, 1);
}

function getSheetName(theme) {
    return ("/static/css/gkit_css/themes/gk_theme_" + theme + ".css");
}

$(function(){
    ctheme = readCookie("theme");
    if (ctheme != null && ctheme.length > 0) {
        changeTheme(ctheme);
    } else {
        changeTheme("hotline_miami");
        createCookie("theme", "hotline_miami", 1)
    }
});

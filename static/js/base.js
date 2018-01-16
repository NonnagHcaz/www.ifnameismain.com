function pluralize(num, singular, plural){
    return''+ num+' '+(num===1?singular:plural);}

function changeTheme(filename) {
    themeBaseDir = "css/gkit_css/themes/"
    newstylesheet = (
        "{% static '" + themeBaseDir + "style_" + filename + ".css' %}");

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
}

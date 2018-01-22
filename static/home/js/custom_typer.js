// Wrapper for TinyTyper.js

$(document).ready(function() {
    var el       = document.querySelector('#message')
    var options  = {
        text: (
            "Initializing content...\n" +
            "Content initialized.\n\n" +
            "Enter username:\n" +
            "$> Retr0\n" +
            "Enter password:\n" +
            "$> *****************\n\n" +
            "Welcome Retr0.\n" +
            "$> "
            ),
        textSpeed: 75,
        blinkSpeed: 0.05,
        cursor: "_"
    }
    var instance = new tinytyper(el, options)
});

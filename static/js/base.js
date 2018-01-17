COOKIE_POLICY_COOKIE_KEY = "policy_acknowledged";

function pluralize(num, singular, plural){
    return''+ num+' '+(num===1?singular:plural);}

function acknowledgeCookiePolicy(){
    createCookie(COOKIE_POLICY_COOKIE_KEY, "True", 1);
    hideCookiePolicy();
}

function hideCookiePolicy(){
    $("#cookie_policy_banner").hide();
}

$(function(){
    var policy_read = readCookie(COOKIE_POLICY_COOKIE_KEY);
    if (policy_read != null) {
        hideCookiePolicy();
    }
})

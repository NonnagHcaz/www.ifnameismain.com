var timer, fullText, currentOffset, onComplete;

function Speak(text) {
    fullText = text;
    currentOffset = 0;
    timer = setInterval(onTick, 50);
}

function onTick() {
    currentOffset++;
    if (currentOffset == fullText.length) {
        complete();
        return;
    }
    var text = fullText.substring(0, currentOffset);
    $("#message").html(text);
}

function complete() {
    clearInterval(timer);
    timer = null;
    $("#message").html(fullText);
    onComplete();
}

window.onload = function() {
    messages = [];
    chat();
};

function chat() {
    var result = "";
    messages.forEach(function(item) {
        if (item.sender == "me") {
            result += "<div id=\"message\">" + item.text + "</div>" + "<br></br>";
        } else {
            result += "<div id=\"messageF\">" + item.text + "</div>" + "<br></br>";
        }
    });

    document.getElementById("messages").innerHTML = result;
}

function handleClick(event) {
    var messageInput = document.getElementById("messageForm");
    var messageText = messageInput.value;

    if (!Array.isArray(messages)) {
        messages = [];
    }
    var sender = "me";
    if(messageText.startsWith("you")) {
        
        sender = "you";
    }
    messages.push({ text: messageText, sender: sender });

    chat();
    messageInput.value = "";
    pane.scrollTop = pane.scrollHeight;

    event.preventDefault();
}


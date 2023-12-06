window.onload = function() {
    chat();
};

  var messages = [
    {text : "Malcom",sender:"me"},
    {text : "Kaylee",sender:"you"},
    {text : "Jayne",sender:"me"},
  ];

function chat() {
    var result = "";
    messages.forEach(function(item){
        if(item.sender == "me"){
            result += "<div id=\"message\">" + item.text + "</div>" + "<br></br>";
        } else {
            result += "<div id=\"messageF\">" + item.text + "</div>" + "<br></br>";
        }
    });

    document.getElementById("messages").innerHTML = result
}

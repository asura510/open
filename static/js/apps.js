function startDictation() {

    if (window.hasOwnProperty('webkitSpeechRecognition')) {

      var recognition = new webkitSpeechRecognition();

      recognition.continuous = false;

      recognition.lang = "en-IN";
      recognition.start();

      recognition.onresult = function(e) {
	      result=e.results[0][0].transcript;

	      recognition.stop();
        rsubmit(result);
      };

      recognition.onerror = function(e) {
        recognition.stop();
      }

    }
  }

function rsubmit(command)
{
    var xhttp = new XMLHttpRequest();
	responsiveVoice.setDefaultVoice("Hindi Female");
	document.getElementById("chatbox").innerHTML += '<div id="sent" class="mdl-color--white mdl-shadow--2dp mdl-cell mdl-cell-align-left mdl-cell--12-col mdl-grid innertext" ><p class="innertext">'+command+'</p></div>';
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
	    response=this.responseText;
     document.getElementById("chatbox").innerHTML += response;
    }
  };
  xhttp.open("GET", "/chatbot/"+command, true);
  xhttp.send();
}
var showDialogButton = document.querySelector('#voice-dialog');
    showDialogButton.addEventListener('click', function() {
      startDictation();
    });
function send_msg(event){
    if (event.key === "Enter") {
        var x= document.getElementById("command").value;
	   rsubmit(x)
    }
}
function say(text){
responsiveVoice.speak(text)
}

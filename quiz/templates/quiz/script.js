
$( document ).ready(function() {
    console.log( "ready!" );
});


$(".answerbox").click(function(){
	alert("I am an alert box!");
	$(this).addClass("answerbox_checked");
});


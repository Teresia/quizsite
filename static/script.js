$( document ).ready(function() {
    console.log( "readyyyyyy!" );



$(".answerbox").click(function(){
	$(".answerbox").removeClass("answerbox_checked");
	$(this).addClass("answerbox_checked");
	});

});
$( document ).ready(function() {
    console.log( "readyyyyyy!" );

$(".answerbox").click(function(){
	$(".answerbox").removeClass("answerbox_checked");
	$(this).addClass("answerbox_checked");
	});

// {% for quiz in quizzes %}
// if ({{ correct }}/{{ total }} ) == 1{
// 	$( "#result" ).replaceWith( "<h1>Alla rätt!</h1>" );
// }
// {% endfor %}



});
$( document ).ready(function() {
    console.log( "readyyyyyy!" );

$(".answerbox").click(function(){
	$(".answerbox").removeClass("answerbox_checked");
	$(this).addClass("answerbox_checked");
	console.log( "readyyyyyy!" );
	$("#fooID").addClass("fooClass");
	setTimeout(function(){
			$(".submit-button").trigger("click")
		}, 1100);

	});

// {% for quiz in quizzes %}
// if ({{ correct }}/{{ total }} ) == 1{
// 	$( "#result" ).replaceWith( "<h1>Alla rätt!</h1>" );
// }
// {% endfor %}



});
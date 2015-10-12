//script for personal page

$(document).ready(function(){
	console.log("it's working");
	$('div.hidden').fadeIn(2000).removeClass("hidden");
	//$('div.slideR').animate({left: "1000px"}, 1000); //creating excess space on right side.
	$('div.slideL').animate({right: "500px"}, 1000);
});
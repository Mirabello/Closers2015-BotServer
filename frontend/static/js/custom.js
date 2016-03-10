$(document).ready(function(){

	// var jumbotron = $("#home");
	// var homePage = function(){
		// jumbotron.addClass("slime")
	// 	}

	// $(jumbotron).delay(1000).queue(function(){
 //        $(this).addClass("slime").clearQueue();
 //     });
	// homePage()
	// var url = "url('/static/img/bot-man.jpg')"
	// console.log(url)
	// $(jumbotron).css("background-image", url)


var mainbottom = $('#home').offset().top + $('#home').height();
// on scroll, 
$(window).on('scroll',function(){
    // we round here to reduce a little workload
    var stop = Math.round($(window).scrollTop());
    if (stop > mainbottom) {
        $('.navbar').addClass('past-main');
    } else {
        $('.navbar').removeClass('past-main');
   }

});


});
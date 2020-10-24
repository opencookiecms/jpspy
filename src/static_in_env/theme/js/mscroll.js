(function($) {
    "use strict";
	
	$(".imagescroll").mCustomScrollbar({
		axis:"x",
		theme:"dark-3",
		advanced:{ autoExpandHorizontalScroll:true }
	});
	$(".scroll-1").mCustomScrollbar({
		theme:"dark"
	});
	$(".vscroll").mCustomScrollbar();
	
})(jQuery);
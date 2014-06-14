$(document).ready(function () {

	$("#content .alt").live("click", function() {
		alert($(this).text());
	});

}
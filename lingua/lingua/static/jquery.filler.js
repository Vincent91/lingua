$(document).ready(function () {

	$("#content").on("click", "td", function() {
		var aes = $(this).attr("attributeES");
		var ais = $(this).attr("attributeIS");
		var aisa = $(this).attr("attributeISA");
		var aip = $(this).attr("attributeIP");
		var aipa = $(this).attr("attributeIPA");
		$("#myModal").html("<h1>" + aes + "</h1><h2>" + aisa + " " + ais + "</h2><h2>" + aipa + " " + aip + 
			"</h2><a class='close-reveal-modal'>&#215;</a>");
		$("#revelator").click();
	});

});
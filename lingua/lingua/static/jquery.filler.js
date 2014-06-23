$(document).ready(function () {

	$("#content.nounContent").on("click", "td", function() {
		var aes = $(this).attr("attributeES");
		var ais = $(this).attr("attributeIS");
		var aisa = $(this).attr("attributeISA");
		var aip = $(this).attr("attributeIP");
		var aipa = $(this).attr("attributeIPA");
		var htmlString = "<h2>English form</h1>";
		htmlString += "<p>" + aes + "</p>";
		htmlString += "<h2>Italian singular form</h2>";
		htmlString += "<p>" + aisa + " " + ais + "</p>";
		htmlString += "<h2>Italian plural form</h2>";
		htmlString += "<p>" + aipa + " " + aip + "</p>";
		htmlString += "</h2><a class='close-reveal-modal'>&#215;</a>";
		$("#myModal").html(htmlString);
		$("#revelator").click();
	});

	$("#content.verbContent").on("click", "td", function() {
		var aei = $(this).attr("attributeEI");
		var aii = $(this).attr("attributeII");
		var aic = $(this).attr("attributeIC");
		var aio = $(this).attr("attributeIO");
		var atu = $(this).attr("attributeTU");
		var alei = $(this).attr("attributeLEO");
		var anoi = $(this).attr("attributeNOI");
		var avoi = $(this).attr("attributeVOI");
		var aessi = $(this).attr("attributeESSI");
		var htmlString = "<h2>English form</h2>";
		htmlString += "<p>" + aei + "</p>";
		htmlString += "<h2>Italian form</h2>";
		htmlString += "<p>" + aii + " " + aic + "</p>";
		htmlString += "<h2>Italian " + aic + " singular</h2>";
		htmlString += "<p><b>Io </b>" + aio + "</p>";
		htmlString += "<p><b>Tu </b>" + atu + "</p>";
		htmlString += "<p><b>Lei </b>" + alei + "</p>";
		htmlString += "<h2>Italian " + aic + " plural</h2>";
		htmlString += "<p><b>Noi </b>" + anoi + "</p>";
		htmlString += "<p><b>Voi </b>" + avoi + "</p>";
		htmlString += "<p><b>Essi </b>" + aessi + "</p>";
		htmlString += "</h2><a class='close-reveal-modal'>&#215;</a>";
		$("#myModal").html(htmlString);
		$("#revelator").click();
	});

});
$(document).ready(function () {

	$("#content.nounContent").on("click", "td", function() {
		var aes = $(this).attr("attributeES");
		var ais = $(this).attr("attributeIS");
		var aisa = $(this).attr("attributeISA");
		var aip = $(this).attr("attributeIP");
		var aipa = $(this).attr("attributeIPA");
		var htmlString = "<h2>English form</h1>";
		htmlString += "<p>" + aes + "</p>";
		htmlString += "<div><div style='float:left;'>";
		htmlString += "<h2>Italian singular</h2>";
		htmlString += "<p>" + aisa + " " + ais + "</p></div>";
		htmlString += "<div style='float:left;margin-left:2em;'><h2>Italian plural</h2>";
		htmlString += "<p>" + aipa + " " + aip + "</p></div>";
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
		var alei = $(this).attr("attributeLEI");
		var anoi = $(this).attr("attributeNOI");
		var avoi = $(this).attr("attributeVOI");
		var aessi = $(this).attr("attributeESSI");
		var htmlString = "<h2>English form</h2>";
		htmlString += "<p>" + aei + "</p>";
		htmlString += "<h2>Italian form (" + aic + ")</h2>";
		htmlString += "<p>" + aii + "</p>";
		htmlString += "<div><div style='float:left;'>";
		htmlString += "<h2>Italian singular</h2>";
		htmlString += "<p><b>Io </b>" + aio + "</p>";
		htmlString += "<p><b>Tu </b>" + atu + "</p>";
		htmlString += "<p><b>Lei </b>" + alei + "</p></div>";
		htmlString += "<div style='float:left;margin-left:2em;'><h2>Italian plural</h2>";
		htmlString += "<p><b>Noi </b>" + anoi + "</p>";
		htmlString += "<p><b>Voi </b>" + avoi + "</p>";
		htmlString += "<p><b>Essi </b>" + aessi + "</p></div>";
		htmlString += "</h2><a class='close-reveal-modal'>&#215;</a>";
		$("#myModal").html(htmlString);
		$("#revelator").click();
	});

	$("#content.adjectiveContent").on("click", "td", function() {
		var aef = $(this).attr("attributeEF");
		var aism = $(this).attr("attributeISM");
		var aisf = $(this).attr("attributeISF");
		var aipm = $(this).attr("attributeIPM");
		var aipf = $(this).attr("attributeIPF");
		var htmlString = "<h2>English form</h2>";
		htmlString += "<p>" + aef + "</p>";
		htmlString += "<div><div style='float:left;'>"
		htmlString += "<h2>Italian singular</h2>";
		htmlString += "<p><b>Masculine</b> " + aism + "</p>";
		htmlString += "<p><b>Feminine</b> " + aisf + "</p></div>";
		htmlString += "<div style='float:left;margin-left:2em;'><h2>Italian plural</h2>";
		htmlString += "<p><b>Masculine</b> " + aipm + "</p>";
		htmlString += "<p><b>Feminine</b> " + aipf + "</p></div>";  
		htmlString += "</h2><a class='close-reveal-modal'>&#215;</a>";
		$("#myModal").html(htmlString);
		$("#revelator").click();
	});

	$("#content.miscContent").on("click", "td", function() {
		var aep = $(this).attr("attributeEP");
		var aip = $(this).attr("attributeIP");
		var htmlString = "<h2>English form</h2>";
		htmlString += "<p>" + aep + "</p>";
		htmlString += "<h2>Italian form</h2>";
		htmlString += "<p>" + aip + "</p>";
		htmlString += "</h2><a class='close-reveal-modal'>&#215;</a>";
		$("#myModal").html(htmlString);
		$("#revelator").click();
	});

});
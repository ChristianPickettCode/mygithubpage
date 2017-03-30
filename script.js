$(document).ready(function() {

	var FEED_URL = "http://feeds.gimletmedia.com/hearreplyall?format=xml";

	function postData(input) {
	    $.ajax({
	        type: "POST",
	        url: "/parser.py",
	        data: { param: input },
	        success: callbackFunc
	    });
	}

	function callbackFunc(response) {
	    // do something with the response
	    console.log(response);
	    console.log("success");
	}

	console.log("Start");
	postData()


});
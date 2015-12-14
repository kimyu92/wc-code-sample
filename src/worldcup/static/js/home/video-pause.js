// Pause button functionality

$(document).ready(function(){
	var $vid = $("#bgvid");
	var $pauseButton = $("#bgvid-btn");

	function vidFade() {
	    $vid.addClass("stopfade");
	}

	$vid.on('ended', function() {
	    // only functional if "loop" is removed 
	    var vid = $vid[0];
	    vid.pause();
		// to capture IE10
		vidFade();
	});

	$pauseButton.on("click", function() {
	    $vid.toggleClass("stopfade");
		
		var vid = $vid[0];

		if (vid.paused) {
			vid.play();
			$pauseButton.innerHTML = "Pause";
		}
		else {
	        vid.pause();
	        $pauseButton.innerHTML = "Paused";
		}
	});
});
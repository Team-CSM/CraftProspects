soundEfx = document.getElementById("soundEfx");
vid = document.getElementById("intro");
tvoff = document.getElementById("tvoff");


//on page load, ensure parallax initialised
$(document).ready(function () {
  $('.parallax').parallax();
});

// Removes a div from it's parent. Used when removing the game overlay from the container.
function removeElement(parentDiv, childDiv) {
  if (childDiv == parentDiv) {
    alert("The parent div cannot be removed.");
  }
  // if the overlay is removed, play the select audio clip, and play the video.
  else if (document.getElementById(childDiv)) {
    soundEfx.play();
    var child = document.getElementById(childDiv);
    var parent = document.getElementById(parentDiv);
    parent.removeChild(child);
    $("#intro").removeClass("hidden");
    $("#jump").removeClass("hidden");
    vid.play();
  }
  else {
    alert("Child div has already been removed or does not exist.");
    return false;
  }

}
var offset = $('#top_link').offset().top;
var navbar = $('.nav-y');


// Changes the Navigation to be above the CRT scanlines at a certain offset.
$(document).scroll(function () {
  position = $(this).scrollTop();
  if (position < offset) {
    navbar.css('z-index', '999');
  } else {
    navbar.css('z-index', '10000');
  }
});

// Refreshes page when called
function Refresh() {
  window.parent.location = window.parent.location.href;
}

document.getElementById('intro').addEventListener('ended', playGame, false);

// Closes the video overlay, and instantiates the game instance.
function playGame(e) {
  $("#intro").addClass("hidden");
  $("#jump").addClass("hidden");
  $("#gameContainer").removeClass("hidden");
  var gameInstance = UnityLoader.instantiate("gameContainer", "Build/FinalGL2.json", { onProgress: UnityProgress });
  $("#nav").addClass("hidden");
  tvoff.play();
  document.getElementById("rest").style.marginTop = "100vh";
}

var myvideo = document.getElementById('intro'),
  jumplink = document.getElementById('jump');

// Skips the video to the end time when pressed.
jumplink.addEventListener("click", function (event) {
  event.preventDefault();
  myvideo.play();
  myvideo.pause();
  myvideo.currentTime = 62;
  myvideo.play();
}, false);
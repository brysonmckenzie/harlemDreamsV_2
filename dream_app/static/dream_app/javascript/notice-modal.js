  var exitBtn = document.getElementById("notice-exit");
//   var flow = document.querySelector("body")
  var modal = document.querySelector(".")

  $(window).on('beforeunload', function () {
    $('body').hide();
    $(window).scrollTop(0);
  });


  exitBtn.onclick = function () {

    modal.style.display = "none";
    flow.style.overflowY = "scroll";

    console.log("working")

  }
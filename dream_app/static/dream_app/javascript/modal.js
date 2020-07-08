

// var span =  document.getElementsByClassName("ex")[0];


// console.log('working')

// function clearModal() {
//     modal.style.display = "none";
// }

// window.onclick = function(event) {
//     if (event.target === span) {
//         clearModal();
//     }
// }

var exitBtn = document.getElementsByClassName("ex")[0];
  var flow = document.querySelector("body")
  var modal = document.querySelector("vid-modal")

  $(window).on('beforeunload', function () {
    $('body').hide();
    $(window).scrollTop(0);
  });


  exitBtn.onclick = function () {

    modal.style.display = "none";
    flow.style.overflowY = "scroll";

    console.log("working")

  }
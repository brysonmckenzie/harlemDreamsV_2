

var span =  document.getElementsByClassName("ex")[0];


console.log('working')

function clearModal() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target === span) {
        clearModal();
    }
}


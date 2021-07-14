const color_blue = '#1a73e8';
const color_gray = '#222222';
var form_container = null;
var margin_top = 50

window.onload = () => {


    // Setup the form
    form_container = document.querySelector('#form-container');
    document.querySelectorAll("p").forEach(field => {
        var label = field.querySelector('label');
        var input = field.querySelector('input');

        label.textContent = label.textContent.slice(0, -1);

        input.onfocus = function(){ setFocusStatePosition(label, input) };
        input.addEventListener("focusout", ()=> setInactiveStatePosition(label, input) );

        setInactiveStatePosition(label, input);
        label.style.transitionDuration = '.2s';
    });
};

function setInactiveStatePosition(label: HTMLLabelElement, input: HTMLInputElement){
    if (input.value != ''){
        label.style.color = color_gray;
        return;
    }

    var bb = input.getBoundingClientRect();
    var offset = bb.height / 2;
    label.style.left = offset * 2 + 'px';
    label.style.top = bb.y - margin_top + offset - label.clientHeight / 2 - 2 + 'px';
    label.style.fontSize = '1.2rem';
    
    label.style.color = color_gray;
}

function setFocusStatePosition(label: HTMLLabelElement, input: HTMLInputElement){
    var bb = input.getBoundingClientRect();
    var offset = bb.height / 2;
    label.style.left = offset * 1.75 + 'px';
    label.style.fontSize = '1rem';
    label.style.top = bb.y - margin_top - label.clientHeight / 2 + 'px';
    label.style.color = color_blue;
}
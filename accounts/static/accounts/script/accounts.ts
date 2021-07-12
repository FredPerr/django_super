const color_blue = '#1a73e8';
const color_gray = '#222222';

window.onload = () => {

    // Setup the form
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

function getPosition(obj){
    var curleft= 0, curtop = 0;
    if (obj.offsetParent) {
        do {
			curleft += obj.offsetLeft;
			curtop += obj.offsetTop;
        } while (obj = obj.offsetParent);
    }
    return [curleft, curtop]
}


function setInactiveStatePosition(label: HTMLLabelElement, input: HTMLInputElement){
    if (input.value != ''){
        label.style.color = color_gray;
        return;
    }

    var bb = input.getBoundingClientRect();
    var pos = getPosition(input);
    var offset = bb.height / 2;
    label.style.left = offset * 2 + 'px';
    label.style.top = pos[1] + offset - label.clientHeight / 2 - 1 + 'px';
    label.style.fontSize = '1.2rem';
    
    label.style.color = color_gray;
}

function setFocusStatePosition(label: HTMLLabelElement, input: HTMLInputElement){
    var bb = input.getBoundingClientRect();
    var offset = bb.height / 2;
    label.style.left = offset * 1.75 + 'px';
    label.style.fontSize = '1rem';
    label.style.top = bb.y - label.clientHeight / 2 + 'px';
    label.style.color = color_blue;
}
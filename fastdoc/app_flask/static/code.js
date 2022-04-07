function serializeSCasePic() {
    let elements = document.getElementsByClassName("s-case-pics");
    for (var i = 0; i < elements.length; i++) {
        console.log(i);
    }
}

function serializeFields() {
    serializeSCasePic();
}

function submitForm(event) {
    event.preventDefault();
    serializeFields();
}

function createSortables() {
    
    let elements = document.getElementsByClassName("sortable");
    for (var i = 0; i < elements.length; i++) {
        new Sortable(elements[i], {
            group: 'shared'
        });
    }
}

function togglePicSelection(el, event) {
    let elements = document.getElementsByClassName("thumb-container");

    if (!event.ctrlKey) {
        for (var i = 0; i < elements.length; i++) {
            if (elements[i] == el) {
                continue;
            }
            elements[i].classList.remove('pic-selected')
        }
    }
    el.classList.toggle('pic-selected');

}



// function configContextMenuCasePics(objects) {

//     let elements = document.getElementsByClassName("tr-case-pics-pics");
//     for (var i = 0; i < elements.length; i++) {
      
//     }
// }
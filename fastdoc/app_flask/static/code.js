function appendElementFromBackEnd(endpoint, container, data, callback){
    axios.post(endpoint, data).then(result => {
        container.innerHTML += result.data;
        callback();
    })
}

function innerHtmlFromBackEnd(endpoint, element, data, callback){
    axios.post(endpoint, data).then(result => {
        element.innerHTML += result.data;
        callback();
    })
}
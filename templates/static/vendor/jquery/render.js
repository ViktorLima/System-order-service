function renderUperCase(){
    $("#seach").toLowerCase().replace(/(?:^|\s)(?!da|de|do)\S/g, l => l.toUpperCase());
}
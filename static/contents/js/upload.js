var changeFontStyle = function (font) {
    document.getElementById(
        "output-text").style.fontFamily
        = font.value;
}
var loadFile = function (event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};
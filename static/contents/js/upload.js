var changeFontStyle = function (font) {
    document.getElementById(
        "output-text").style.fontFamily
        = font.value;
}
var loadFile = function (event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};

function posting(artist) {

    const value = artist
    const file = $('#file')[0].files[0]
    const form_data = new FormData()
    console.log(file)
    form_data.append("image", file)
    form_data.append("value", value)
    console.log(form_data)
    // console.log(artist)

    $.ajax({
        type: "POST",
        url: "http://paintary-nst-dev.ap-northeast-2.elasticbeanstalk.com/fileupload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            let image_url = response['file_url'];
            console.log(image_url);
            $("#styled_img").attr('src', image_url)
            return image_url
        }
    });
}
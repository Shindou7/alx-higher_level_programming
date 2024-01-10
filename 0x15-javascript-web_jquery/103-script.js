const $ = window.$;

$(document).ready(function () {
  $('#btn_translate').click(function () {
    showHello();
  });

  $('#language_code').keydown(function (event) {
    if (event.keyCode === 13) {
      showHello();
    }
  });
});

function showHello() {
  const languageCode = $('#language_code').val();

  $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
    $('#hello').text(data.hello);
  });
}

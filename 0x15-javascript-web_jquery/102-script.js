const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').text();
    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  });
};

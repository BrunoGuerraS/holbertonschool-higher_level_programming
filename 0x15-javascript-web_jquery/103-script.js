function chang(){
    const inputVal = $('input#language_code').val()
    $.ajax(`https://www.fourtonfish.com/hellosalut/?lang=${code}`)
    .done(data => $('div#hello').text(data.hello))
    .fail(err => console.log(err));
}

$(document).ready(function(){
    $('input#btn_translate').on('click', () => translate());
    $('input#language_code').on('keypress', ({ key }) => {
      if (key === 'Enter') translate();
    });
})
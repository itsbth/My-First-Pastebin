$(function(){
  var re = /([^+]+)\+?(.*)/;
  var di = {};
  var li = $('#lang')[0].options;
  var l2 = $('<select></select>').append('<option>N/A</option>');
  $('#lang').attr('name', '');
  l2.attr('name', 'type');
  $('#lang').parent().append(l2);
  for (i in li){
    var ri = re.exec(li[i].value);
    if (ri[2].length > 0)
    {
      if (di[ri[1]] == null) di[ri[1]] = [];
      di[ri[1]].push(ri[2]);
      $(li[i]).hide();
    }
  }
  $('#lang').change(function(){
    var lang = this.value;
    l2.children().remove();
    l2.append($('<option value="' + lang + '">N/A</option>'));
    if (di[lang]){
      for (var i in di[lang])
      {
        l2.append($('<option value="' + lang + '+' + di[lang][i] + '">' + di[lang][i] + '</option>'));
      }
    }
    $('.bespin')[0].bespin.editor.syntax = lang;
  });
  $('form').submit(function(){
    $('textare').value($('.bespin')[0].bespin.editor.value);
  });
});

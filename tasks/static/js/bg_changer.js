$(document).ready(function() {
  var currentPicNum = $.cookie('background');
  if (currentPicNum==null) {
    currentPicNum = Math.floor((Math.random() * 7) + 1).toString();
    $.cookie('background', currentPicNum, { expires: 7, path: ['/', '/login']});
  }

  $('body').css('background-image', 'url("' + 'static/images/'+ currentPicNum +'.jpg")');

  $('#change_bg').on('click', function(){
    var picNum = Math.floor((Math.random() * 7) + 1).toString();
    $('body').css('background-image', 'url("' + 'static/images/'+ picNum +'.jpg")');
    $.cookie('background', picNum);
  });

});

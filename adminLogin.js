var scrolly = function(e) {
    e.preventDefault();
    var target = this.hash;
    var $target = $(target);
  
    $('html, body').stop().animate({
        'scrollTop': $target.offset().top
    }, 300, 'swing', function () {
        window.location.hash = target;
    });
  }
  
  var init = function() {
    burger.addEventListener('click', openMenu, false);
    window.addEventListener('scroll', scrollFx, false);
    window.addEventListener('load', scrollFx, false);
    $('a[href^="#"]').on('click',scrolly);
  };
  
  doc.on('ready', init);
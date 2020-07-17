let inicio = document.querySelector('.menu1');
let bar = document.querySelector('.bar');
let seccion1 = document.querySelector('.caja-seccion1');

/* FLECHA SCROLL*/

$(function() {
  $('a[href*=#]').on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: $($(this).attr('href')).offset().top}, 500, 'linear');
  });
});
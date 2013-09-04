$('#lz-carousel').carousel({
  interval: 6000
});

$('.lz-carousel-navi a').on('click', function(event){
    event.preventDefault();
    $('.lz-carousel-navi').children().removeClass('active');
    $(this).addClass("active");
});

$('#lz-carousel').on('slid', function() {
    var to_slide = $('.carousel-inner .item.active').attr('id');
    $('.lz-carousel-navi').children().removeClass('active');
    $('.lz-carousel-navi [data-slide-to=' + to_slide + ']').addClass('active');
});

$('.ui-carousel-link').on('click', function(event) {
    event.preventDefault();
    window.location = $(this).attr('data-href');
});

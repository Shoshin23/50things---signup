jQuery(document).ready(function() {

    /*
        Background slideshow
    */
    $('.coming-soon').backstretch([
      "static/img/backgrounds/1.jpg"
    , "static/img/backgrounds/2.jpg"
    , "static/img/backgrounds/3.jpg"
    , "static/img/backgrounds/4.jpg"
    , "static/img/backgrounds/5.jpg"
    , "static/img/backgrounds/6.jpg"
    ], {duration: 3000, fade: 750});

    /*
        Countdown initializer
        var now = new Date();
    var countTo = 25 * 24 * 60 * 60 * 1000 + now.valueOf();
    $('.timer').countdown(countTo, function(event) {
        var $this = $(this);
        switch(event.type) {
            case "seconds":
            case "minutes":
            case "hours":
            case "days":
            case "weeks":
            case "daysLeft":
                $this.find('span.'+event.type).html(event.value);
                break;
            case "finished":
                $this.hide();
                break;
        }
    });

    */
});

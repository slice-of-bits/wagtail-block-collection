// Set the date we're counting down to
CountDownElement = document.getElementById("countdown")

if(CountDownElement) {
    var countDownDate = new Date(CountDownElement.getAttribute("data-to-date")).getTime();

    // Update the count down every 1 second
    var x = setInterval(function () {

        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="demo"

        countdownString = '';

        if (CountDownElement.getAttribute('data-days-string')) {
            console.log("test");
            countdownString = days + CountDownElement.getAttribute('data-days-string');
        }

        if (CountDownElement.getAttribute('data-hours-string')) {
            countdownString = countdownString + hours + CountDownElement.getAttribute('data-hours-string');
        }

        if (CountDownElement.getAttribute('data-minutes-string')) {
            countdownString = countdownString + minutes + CountDownElement.getAttribute('data-minutes-string');
        }

        if (CountDownElement.getAttribute('data-seconds-string')) {
            countdownString = countdownString + seconds + CountDownElement.getAttribute('data-seconds-string');
        }

        CountDownElement.innerHTML = countdownString;

        // If the count down is finished, write some text
        if (distance < 0) {
            clearInterval(x);
            CountDownElement.innerHTML = "EXPIRED";
        }
    }, 1000);
}
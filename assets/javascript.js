(function () {
    var start = Date.now(),
        diff,
        duration,
        minutes,
        RUN=1,
        seconds;
    function timer() {
    if (RUN==1){      
      duration = 3;
        // get the number of seconds that have elapsed since 
        // startTimer() was called
        diff = duration - (((Date.now() - start) / 1000) | 0);

        // does the same job as parseInt truncates the float
        minutes = (diff / 60) | 0;
        seconds = (diff % 60) | 0;

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

	document.getElementById("minutes").innerText=minutes;
  document.getElementById("seconds").innerText=seconds;
    }
        if (diff <= 0) {
          document.getElementById("headline").innerText = "Times up!";
          clearInterval();
          RUN =0;
            // add one second so that the count down starts at the full duration
            // example 05:00 not 04:59
            //start = Date.now() + 1000;
        }
    };
    // we don't want to wait a full second before the timer starts
    timer();
    setInterval(timer, 1000);
  }());



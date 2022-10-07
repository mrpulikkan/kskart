
            setTimeout(function(){
                $('#preloader').fadeToggle();
            }, 1000);


            var slideImg = document.getElementById("slideImg");
            var images = new Array(
                "{% static 'images/veg1.jpg' %}",
                "{% static 'images/veg3.jpg' %}",
                "{% static 'images/nb1.jpg' %}",
                "{% static 'images/veg4.jpg' %}"
            );
            var len = images.length;
            var i = 0;
            function slider(){
                if(i > len-1){
                    i = 0;
                }
                slideImg.src = images[i];
                i++;
                setTimeout('slider()',3000);
            }

            window.addEventListener('scroll', reveal);
            function reveal(){
                var reveals = document.querySelectorAll('.reveal')

                for(i = 0; i < reveals.length; i++){
                    var windowHeight = window.innerHeight
                    var revealtop = reveals[i].getBoundingClientRect().top;
                    var revealpoint = 150;


                    if(revealtop < windowHeight - revealpoint){
                        reveals[i].classList.add('active');
                    }
                    else{
                        reveals[i].classList.remove('active');
                    }
                }
            }

       
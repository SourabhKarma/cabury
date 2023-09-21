$(document).ready(function(){

    $(function(){
        $("#btn_redeem").click(function(){
            $("#modal_coupon").fadeIn();
        });
        $("#btn_close_modal").click(function(){
            $("#modal_coupon").css("display","none");
        });
    });

    $(function(){
        var cpnBtn = document.getElementById("cpnBtn");
        var cpnCode = document.getElementById("cpnCode");

        cpnBtn.onclick = function(){
            navigator.clipboard.writeText(cpnCode.innerHTML);
            cpnBtn.innerHTML ="COPIED";
            setTimeout(function(){
                cpnBtn.className  = 'fa fa-copy'
                cpnBtn.innerHTML ="";
            }, 3000);
        }
    }); 

    $(function(){
        $(".group_block").slice(0,1).show();
        $("#loadmore").click(function(e){
          e.preventDefault();
          $(".group_block:hidden").slice(0,1).fadeIn("slow");
          
          if($(".group_block:hidden").length == 0){
             $("#loadmore").attr("disabled",true);
            }
        });
    });
    $(function(){
        window.onload = function(){
            let player = document.getElementById("player"),
                play = document.getElementById("play");
            play.addEventListener("click",function(){
              player.play();
            });
          }
    });

    $(function(){
        $('#btn_openModal').click(function(){
            let pattern1 = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
            let result1 = pattern1.test($('#email').val())
            if($('#phone').val() == ''){
               alert('Phone can not be left blank and atleast 10 char long');
               return false;
            }
            if($('#name').val() == '') {
               alert('Name can not be left blank');
               return false;
            }

            if(!result1) {

                alert('Email can not be left blank and it should be @');
                return false;
             }
            $('#addEventModal').addClass('modal_active');
            return true;
            
         });
    });

    $(function(){
        $(window).on("load",function(){
            $(".scroll_content").mCustomScrollbar({
                theme:"dark",
            });
        });
    });
    $(function(){
        $(window).on("load",function(){
            $(".list_content").mCustomScrollbar({
                theme:"dark",
            });
        });
    });

    $(function(){
        $("#btn_menuhamburger").click(function(){
            $(".right_sidebar").addClass('right_sidebar_active')
            $(".overlay").addClass('overlay_active')
        });
        $("#btn_close").click(function(){
            $(".right_sidebar").removeClass('right_sidebar_active')
            $(".overlay").removeClass('overlay_active')
        });
    });
    $(function(){
        AOS.init({
            duration: 1200,
        });
    });
})
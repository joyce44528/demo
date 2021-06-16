$(document).ready(function () {
    $('.navigation__link').on('click',function(e){
        e.preventDefault(); 
        var target = $(this).attr('href');
        var targetPos = $(target).offset().top+90;
     //     知道y軸的偏移量

        // 處理點選nav__link時要將navigation取消選取
        if ($('#nav-toggle').prop("checked")) {
            $("input[class=navigation__checkbox]").prop("checked",false);
            $('html, body').delay("slow").animate({scrollTop: targetPos}, 1400);
        }
           
        
    })
    // 視差滾動
    $(window).scroll(function(){
        //     用一變數儲存scroll時的位置
            var scrollPos = $(window).scrollTop();  //滾動的值
            var windowHeight = $(window).height();//     注意這個一定要加!
            
         $('.animated').each(function(){
            var thisPos = $(this).offset().top;
            if((windowHeight + scrollPos) >= thisPos*1.1) {
                console.log("animated", thisPos,windowHeight + scrollPos);
                $(this).addClass('fadeIn');
            }
        });
            
    });




});

    

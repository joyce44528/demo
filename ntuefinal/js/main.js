
$(document).ready(function () {
    
    $('.navigation__link,.btn--animate,.btn-text--linkbook').on('click',function(e){
        e.preventDefault(); 
        var target = $(this).attr('href');
        var targetPos = $(target).offset().top+50;
     //     知道y軸的偏移量

        // 處理點選nav__link時要將navigation取消選取
        if ($('#nav-toggle').prop("checked")) {
            $("input[class=navigation__checkbox]").prop("checked",false);
            
        }
    
        $('html, body').delay("slow").animate({scrollTop: targetPos}, 1400);    
        
    })

    // scroll up需要另外設定 因為它沒辦法使用同一個變數
    $('.scroll-up').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({scrollTop: 0}, 1400); 
    });
    // 視差滾動
    $(window).scroll(function(){
        //     用一變數儲存scroll時的位置
            let scrollPos = $(window).scrollTop();  //滾動的值
            let windowHeight = $(window).height();//     注意這個一定要加!
            

         $('.animated').each(function(){
            let thisPos = $(this).offset().top;

            if((windowHeight + scrollPos) >= thisPos) {
                // console.log("animated", thisPos,windowHeight + scrollPos);
                $(this).addClass('fadeIn');
            }
        });


        // 調整nav的顏色，當超出header範圍，則呈現白色
        // 調整scroll-up的出現與否
        $('.scroll').each(function(){
            let headerhight = ($(this).height() - 100);
           
            if(headerhight < scrollPos){
                $('.navigation__button').addClass('navigation__color');
                $('.scroll-up').css({'transform':'translateY(0)'});
            }
            if(headerhight >= scrollPos){
                $('.navigation__button').removeClass('navigation__color');
                $('.scroll-up').css({'transform':'translateY(160%)'});
            }
            
        });
             
        // header-secondary的視差滾動
        $('.heading-secondary').each(function(){
            let thisPos = $(this).offset().top;
            // console.log("header-secondary", thisPos,windowHeight + scrollPos);

            if((windowHeight + scrollPos) >= thisPos) {
                
                $(this).addClass('header-layer');
            }

        });

        // 調整book-wrap背景顏色，當超出section__book1範圍，就換顏色
        $('.section__book-2').each(function(){
            let thisPos = $(this).offset().top;
            // let thisheight = $(this).height();
           

            if((windowHeight + scrollPos) >= thisPos*1.1) {
                $('.book-wrap').addClass('bg-color');
            }
            else{
                $('.book-wrap').removeClass('bg-color');
                // $(this).siblings().css("opacity", "1")
            }
            
            
            
        });

        $('.section__book-3').each(function(){
            let thisPos = $(this).offset().top;
            // let thisheight = $(this).height();
           

            if((windowHeight + scrollPos) >= thisPos*1.1) {
                $('.book-wrap').addClass('bg-color-2');
            }
            else{
                $('.book-wrap').removeClass('bg-color-2');
                // $(this).siblings().css("opacity", "1")
            }
            
            
            
        });

        $('.section__book-4').each(function(){
            let thisPos = $(this).offset().top;
            // let thisheight = $(this).height();
           

            if((windowHeight + scrollPos) >= thisPos*1.1) {
                $('.book-wrap').addClass('bg-color-3');
            }
            else{
                $('.book-wrap').removeClass('bg-color-3');
                // $(this).siblings().css("opacity", "1")
            }
            
            
            
        });


            
    });

    // flexslider輪播
    $(function() {
        $(".flexslider").flexslider({
            slideshow: true,
            slideshowSpeed: 5000, //展示时间间隔ms
            animationSpeed: 500, //滚动时间ms
            touch: true, //是否支持触屏滑动
            directionNav: false
        });
    });	

    // 點擊展開收合
    $(".detail-toggle").click(function () { 
        
        $(".detail-content").slideToggle();
        
    });


   

});

let sendButton = document.querySelector('#submit-btn');

// 加上.trim()去除內容的前後空白字元
function send() {
  let name = document.querySelector('#name').value.trim();
  let sex = document.querySelector('input[name="sex"]:checked'); 
  let departmentLevel = document.querySelector('#department-level').value.trim();
  let yourReason = document.querySelector('#your-reason').value.trim();
  let webFeeling = document.querySelector('#web-feeling').value.trim();
  let status = true;


// 避免交出空表單
  if(name == ''){
    document.querySelector('#name').style.border = '1px solid #C86649';
    status = false;
  }
  if(departmentLevel == ''){
    document.querySelector('#department-level').style.border = '1px solid #C86649';
    status = false;
  }
  if(sex == null) {
    alert('請填寫性別');
    status = false;
  }
  if(yourReason == ''){
    alert('請填寫愛上國北的理由喔~');
    status = false;
  }

  if(status) {
      // 增加日期資料
        let currentdate = new Date();
        let filltime = currentdate.getFullYear() + "/"
            + (currentdate.getMonth() + 1) + "/"
            + currentdate.getDate() + "  "
            + currentdate.getHours() + ":"
            + currentdate.getMinutes() + ":"
            + currentdate.getSeconds();
        let data = {
            "name": name,
            "departmentLevel": departmentLevel,
            "sex": sex.value,
            "yourReason": yourReason,
            "webFeeling": webFeeling,
            "time": filltime,
            
        }
        toSend(data);

       
        
    }

   


  

};


function toSend(data){
    sendButton.disabled = 'disabled';
    // 避免連按出現錯誤

    $.ajax({
      // 這邊用get type
      type: "get",
      // api url - google appscript 產出的 url
      url: "https://script.google.com/macros/s/AKfycbyk9P_IficAuD5LUDMR30WaP28D9TccyDJfocVJT1irFSezDyARRE_yul841yYdIH3-/exec",
      // 剛剛整理好的資料帶入
      data: data,
      // 資料格式是JSON 
    //   dataType: "JSON",
      // 成功送出 會回頭觸發下面這塊感謝
      success: function (response) {
        alert('已送出表單~感謝您的填寫！！');
        
        //清空表單內容 
        $(".book__form").find(":text,textarea,input").each(function() {
            $(this).val("");
        });
        $(":radio").attr("checked",false);

        // 送出後重新整理
        window.location.reload();
       
      }
    });
  }


sendButton.addEventListener('click', send);


    

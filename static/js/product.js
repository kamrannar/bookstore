$(document).ready(function(){
    function basket_price(){
        if ($('.price').length>0){
            $('#badge').css('display','block')
            total=0
            $('.price').each(function(i){
                total+=parseInt($(this).text())
                $('#sum').text(total +' AZN')
                $('#badge').text($('.price').length)
            })
        }
        else{
            $('#badge').css('display','none')
            $('#sum').text('0 AZN')
        }
    }
    function unadd(){
        $("#left").removeClass('alert-danger');
        $("#left").addClass('alert-warning');
        $('#add').css('background-color','#109E97')
        $('#add').text('Səbətə əlavə et')
        alert("Məhsul səbətdən çıxarıldı")
        $("#left").text('Bu kitabdan cəmi 2 ədəd qalıb')
        $("#li").remove();
        total=0;
        basket_price()
    }
    $( "#add" ).click(function()  {
        if (add.innerText!='Səbətdən çıxart'){
            $("#left").removeClass('alert-warning');
            $("#left").addClass('alert-danger');
            $('#add').css('background-color','grey')
            $('#add').text('Səbətdən çıxart')
            $("#left").text('Bu kitabdan cəmi 1 ədəd qalıb');
            alert("Məhsul səbətə əlavə edildi")
            $('#basket_list').prepend('<li id="li"></li>')
            $('#li').addClass('mb-2 pe-2 ps-3 justify-content-between d-flex')
            $('#li').prepend('<span id="span2">12 AZN</span>')
            $('#span2').addClass('price')
            $('#li').prepend('<span id="span1">Inkognito</span>')
            $('#span1').addClass('pe-4 ps-3')
            $('#li').prepend('<i id="remove_icon"></i>')
            $('#remove_icon').addClass('fa fa-remove ')
            $('#remove_icon').css('color','red')
            $('#li').first().prepend($('#remove_icon')) 
            $( "#remove_icon" ).click(function() {
                $("#left").removeClass('alert-danger');
                $("#left").addClass('alert-warning');
                $('#add').css('background-color','#109E97')
                $('#add').text('Səbətə əlavə et')
                $("#left").text('Bu kitabdan cəmi 2 ədəd qalıb');
                this.parentNode.parentNode.removeChild(this.parentNode);
                total=0;
                basket_price()
              });
            basket_price()
        } 
        else{
            unadd()
        }
    })    
    $( "#like" ).click(function() {
        if(like.style.color!='blue'){
            $('#like').removeClass('fa-thumbs-up')
            $('#like').addClass('fa-thumbs-down')
            $('#like').css('color','blue')
        }
        else{
            $('#like').removeClass('fa-thumbs-down')
            $('#like').addClass('fa-thumbs-up')
            $('#like').css('color','black')
        }
      } )
    $( "#fav" ).click(function() {
        if(fav.style.color!='red'){
            alert("Kitabı bəyəndiniz!")       
            $('#fav').css('color','red')
        }
        else{
            alert("Bəyənməkdən imtina etdiniz!")
            $('#fav').css('color','black')
        }
    })
    $('#sefiller').click(function (){
        this.parentNode.parentNode.removeChild(this.parentNode);
        total=0;
        $('#badge').text($('.price').length)
        basket_price()
        })
    $('#min').click(function (){
        this.parentNode.parentNode.removeChild(this.parentNode);
        total=0;
        $('#badge').text($('.price').length)
        basket_price()
    })  
    $('.lazy').slick({
        lazyLoad: 'ondemand',
        slidesToShow: 4,
        slidesToScroll: 1
      });
  });
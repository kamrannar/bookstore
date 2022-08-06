$(document).ready(function(){

$('#start').click(function(e3){
    e3.preventDefault();
    let start=$('#start')
    if ($(".btn-warning")[0]){
        start.removeClass('btn-warning')
    start.addClass('btn-danger')
    start.text('Bitir')

    $('#page_counter').append(
        `<div class="row mt-5 " id='extra'>
          <div class="col-5 "><input type="number" min="0" autocomplete=off class="input-group-field w-100" style='border-radius: 6px;'  id="page_count"  value=""></div>
          <div class="col-5 "><input type="number" min="0" autocomplete=off class="input-group-field w-100" id="days" style='border-radius: 6px;' value=""></div>
          <div class="col-2 "><button  id='calc' class='w-100' type='submit' style="background-color:#109E97;color:white;border-color:transparent; border-radius: 6px;width:120px ">Hesabla</button></div>
          </div>`)

    $('#calc').click(function(e3){
        e3.preventDefault();
        let sum=parseInt($('#page_count').val())/parseInt($('#days').val())
        $('#book_alert').remove();
        $('#test').append(
            `<div class="mt-3 alert alert-success w-100 text-center" id='book_alert' role="alert">
             </div>`
        )
        if (isNaN(sum)){
            $('#book_alert').removeClass()
            $('#book_alert').addClass('mt-3 alert alert-danger w-100 text-center')
            $('#book_alert').text('Hesablamada xəta baş verdi!')    
        }
        else{
            $('#book_alert').text('Hər gün ən az '+parseInt(sum)+' səhifə oxumalısınız!')
        }
        })      
    }
    else{
        $('#book_alert').remove();
        start.removeClass('btn-danger')
        start.addClass('btn-warning')
        start.text('Başla')
        $('#extra').remove()
    }    
})

var grid=$('.grid').isotope({
    itemSelector: '.col-3',
    layoutMode: 'fitRows'
  });
  
$('.filter button').click(function(){
    let dataname=$(this).attr('data-name');
    grid.isotope({
        filter:dataname
    })
})
})


let page = parseInt(prompt('Kitabın səhifə sayı:'))
let day = parseInt(prompt('Neçə günə bitirməlisiniz?'))
if(isNaN(page)==true || page==0 || isNaN(day)==true || day==0){
    alert('Hesablamada problem baş verdi')
}
else{
        alert('Hər gün ən az ' + page/day + ' səhifə oxumalısınız!')
        console.log('Səhifə sayı: '+ page)
        console.log('Gün sayı: '+ day)
        console.log('Nəticə: ' + page/day)
}

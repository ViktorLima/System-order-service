 function notUser(){
    let url = window.location.pathname;
    let pagination = $('.page-link');
    let idCustomer = $('#customer_id');
    let userNot =  $('#user-not-found');
    if( url == '/seach/' && idCustomer.length == 0 && pagination.length !== 0){
         pagination.hide();
    }else if(url == '/seach/'&& idCustomer.length !== 0){
         userNot.hide();
    }
 }
notUser();




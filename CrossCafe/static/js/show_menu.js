// Handle all menu page functionalities

displayCart();

function increment(item_id){
    var num = parseInt($('#' + item_id).text());
    $('#' + item_id).text(num+1);
}

function decrement(item_id){
    var num = parseInt($('#' + item_id).text());
    if(num>1)
        $('#' + item_id).text(num-1);
}


// Add item to cart
function addToCart(item_id, item_name){
    var num = parseInt($('#' + item_id).text());
    if(localStorage.getItem('cart')==null)
        var temp = [];
    else
        var temp = JSON.parse(localStorage.getItem('cart'));
    var flag = 0;
    var arrayLength = temp.length;
    if(arrayLength){
        for(var i=0; i<arrayLength; i++){
            if(temp[i]['id'] == item_id){
                temp[i]['quantity']+=num;
                flag = 1;
            }
        }
    }
    if(!flag){
        var item_dict = {'id':item_id, 'item_name':item_name, 'quantity':num};
        temp.push(item_dict);
    }
    console.log(temp);
    localStorage.setItem('cart', JSON.stringify(temp));
}

function checkout(){
    //if(request.user.is_authenticated()){
    //    var data = {'cart': localStorage.getItem('cart'), 'restaurant_id': localStorage.getItem('restaurant_id')};
    //    $.post('/order/createOrder',data,function(response){
    //        console.log(response);
    //    });
    //}
    //else{
       window.location.href = '/order/review';
    //}
}

function displayCart(){
    if(localStorage.getItem('restaurant_id')==null)
        localStorage.setItem('restaurant_id', getQueryStringValue("restaurant_id"));
    else if(localStorage.getItem('restaurant_id')==getQueryStringValue("restaurant_id"))
        if(localStorage.getItem('cart'))
            document.getElementById("cart").innerHTML = localStorage.getItem('cart');
    else{
        localStorage.setItem('restaurant_id', getQueryStringValue("restaurant_id"));
        if(localStorage.getItem('cart'))
            localStorage.removeItem('cart');
    }
}

function getQueryStringValue (key) {  
  return decodeURIComponent(window.location.search.replace(new RegExp("^(?:.*[&\\?]" + encodeURIComponent(key).replace(/[\.\+\*]/g, "\\$&") + "(?:\\=([^&]*))?)?.*$", "i"), "$1"));  
}

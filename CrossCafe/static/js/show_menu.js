// Handle all menu page functionalities

// Add item to cart
function addToCart(item_id){
    if(localStorage.getItem('cart')==null)
        var temp = [];
    else
        var temp = JSON.parse(localStorage.getItem('cart'));
    var flag = 0;
    var arrayLength = temp.length;
    if(!arrayLength){
        var item_dict = {'id': item_id, 'quantity': 1};
        temp.push(item_dict);
        flag = 1;
    }
    else{
        for(var i=0; i<arrayLength; i++){
            if(temp[i]['id'] == item_id){
                temp[i]['quantity']++;
                flag = 1;
            }
        }
    }
    if(!flag){
        var item_dict = {'id': item_id, 'quantity': 1};
        temp.push(item_dict);
    }
    console.log(temp);
    localStorage.setItem('cart', JSON.stringify(temp));
}

function checkout(){
    var data = {'cart': localStorage.getItem('cart')};
    $.post('/order/createOrder',data,function(response){
        console.log(response);
    });
}
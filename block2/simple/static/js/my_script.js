var name;
var manufacturer;
var price;
var rate;
var date;
var image;

function checkButton(){
    btn = document.getElementById("submit-btn");
    if (name && manufacturer && price && rate && date && image)
    {
        btn.removeAttribute("disabled");
    }
    else btn.setAttribute("disabled", true);
}


function namevalidator(form) {
    inp = document.getElementById("name");
    val = inp.value;
    if(val.length == 0){
        name = false;
        inp.setAttribute("placeholder" , "Please enter name");
        inp.setAttribute("style" , "border-color: #f55");
        
    }
    else{
        name = true;
        inp.setAttribute("style" , "border-color: #af8");
    }
checkButton();
      
 }

function manufvalidator(form) {
    inp = document.getElementById("manufacturer");
    val = inp.value;
    if(val.length == 0){
        manufacturer = false;
        inp.setAttribute("placeholder" , "Please enter manufacturer");
        inp.setAttribute("style" , "border-color: #f55");
        
    }
    else{
        manufacturer = true;
        inp.setAttribute("style" , "border-color: #af8");
    }
checkButton();
      
 }

function pricevalidator(form) {
    inp = document.getElementById("price");
    val = inp.value;
    /*if(val % 1 != 0 || val.length == 0)*/
    if((/^[0-9]+$/.test(val)) || (/^[0-9]+\.[0-9]+$/.test(val)) ){
        price = true;
        inp.setAttribute("style" , "border-color: #af8");
        
        
    }
       
    else{
        price  = false;
        inp.setAttribute("placeholder" , "Please enter double number");
        inp.setAttribute("style" , "border-color: #f55");
    }
checkButton();
      
 }

function ratevalidator(form) {
    inp = document.getElementById("rate");
    val = inp.value;
    /*if(val % 1 != 0 || val.length == 0)*/
    if((/^[0-9]+$/.test(val)) || (/^[0-9]+\.[0-9]+$/.test(val)) ){
        rate = true;
        inp.setAttribute("style" , "border-color: #af8");
        
        
    }
       
    else{
        rate  = false;
        inp.setAttribute("placeholder" , "Please enter double number");
        inp.setAttribute("style" , "border-color: #f55");
    }
checkButton();
      
 }
function datevalidator(form) {
    inp = document.getElementById("date");
    val = inp.value;
  
  if ((/(\d{4})-(\d{1,2})-(\d{1,2})/.test(val))){
        date = true;
        inp.setAttribute("style" , "border-color: #af8");
        
        
    }
       
    else{
        date  = false;
        inp.setAttribute("placeholder" , "Please enter date");
        inp.setAttribute("style" , "border-color: #f55");
    }
checkButton();
      
 }
function imagevalidator(){
    inp = document.getElementById("image");
    val = inp.value;
    if (val.length == 0){
        image = false;
        inp.setAttribute("placeholder", "Please attach image");
        inp.setAttribute("style", "border-color: #f55");
    }
    else{
        image = true;
    }
    checkButton();
}


document.getElementById("name").onchange = namevalidator;
document.getElementById("manufacturer").onchange = manufvalidator;
document.getElementById("price").onchange = pricevalidator;
document.getElementById("rate").onchange = ratevalidator;
document.getElementById("date").onchange = datevalidator;
document.getElementById("image").onchange = imagevalidator;




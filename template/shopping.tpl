<!DOCTYPE html>
<html>
<title>362f</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.w3-sidebar a {font-family: "Roboto", sans-serif}
body,h1,h2,h3,h4,h5,h6,.w3-wide {font-family: "Montserrat", sans-serif;}
table, tr{
  border: 1px solid lightgrey;
  border-collapse: collapse;
}
</style>
<body class="w3-content" style="max-width:1200px">

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-bar-block w3-white w3-collapse w3-top" style="z-index:3;width:250px" id="mySidebar">
  <div class="w3-container w3-display-container w3-padding-16">
    <i onclick="w3_close()" class="fa fa-remove w3-hide-large w3-button w3-display-topright"></i>
    <h3 class="w3-wide"><b>Shopping Mall</b></h3>
  </div>
  <div class="w3-padding-64 w3-large w3-text-grey" style="font-weight:bold">
    <a href="/home" class="w3-button w3-block w3-white w3-left-align" id="myBtn">
      Product
    </a>
    <a href="/cart" class="w3-bar-item w3-button">Shopping Cart</a>
    <a href="/history" class="w3-bar-item w3-button">Shopping History</a>
    <a href="/logout" class="w3-bar-item w3-button">Logout</a>
  </div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-bar w3-top w3-hide-large w3-black w3-xlarge">
  <div class="w3-bar-item w3-padding-24 w3-wide">Shopping Mall</div>
  <a href="javascript:void(0)" class="w3-bar-item w3-button w3-padding-24 w3-right" onclick="w3_open()"><i class="fa fa-bars"></i></a>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main " style="margin-left:250px">
  <!-- Push down content on small screens -->
  <div class="w3-hide-large" style="margin-top:83px"></div>
  
  <!-- Top header -->
  <header class="w3-container w3-xlarge">
    <p class="w3-left">Welcome {{name}}</p>
    <p class="w3-right">
      <i class="fa fa-shopping-cart w3-margin-right"></i>
      <i class="fa fa-search"></i>
    </p>
  </header>


  <div class="w3-container w3-text-grey">
    <h3>Shopping cart ({{len(cart.get_cart())}} items)</h3>
    <br><br>
  </div>
%deleteFlag = False
  <!-- Product grid -->
  <div class="w3-row">
  <form action='' method='POST'>
  	<table class="w3-table" id="myTable">
          <th style="width:35%">Product</th>
          <th style="width:20%">Each Price</th>
          <th style="width:20%">Quantity</th>
          <th style="width:20%">Total</th>
          <th style="width:5%"></th>
       <div>
       %for row in cart.get_cart():
       		<tr id='product-row'>
            <td><a href="javascript:void(0)" onclick="warn({{row.item_id}})"> {{row.item_name}} </a></td>
            <td> $ {{row.item_price}} </td>
            <td>
                <input style="width:100%" onclick="UpdateTotal({{row.item_id}},{{row.item_price}});SumTotal()"
                type="number" id="{{row.item_id}}_number" name="{{row.item_id}}_number"
                value={{row.count}} min=1 max={{row.item_quantity}}>
            </td>
            <td id='{{row.item_id}}_total' class="countMe">${{format(float(row.item_price)*int(row.count),'.2f')}}</td>
            <td>
            	<a href = '/delete?id={{row.item_id}}' >
            	<i class="fa fa-times"></i>
                </a>
            </td>
            </tr>
        %end
        <!-- sum -->
        <tr><td></td><td></td><th>Sum:</th><td id='Totalsum'>${{cart.get_total()}}</td><td></td>
        <script>
            function SumTotal(){
                var tds = document.getElementById('myTable').getElementsByTagName('td');
                var sum = 0;
                for(var i = 0; i < tds.length; i ++) {
                    if(tds[i].className == 'countMe') {
                        sum += parseFloat(tds[i].innerHTML.split("$").pop());
                    }
                }
                document.getElementById("Totalsum").innerHTML= '$' + sum.toFixed(2);
            }
        </script>
        <tr>
       </div>
     </table>
     <!-- BUTTON -->
     <br>
     <div>
        <button class='w3-button w3-black' type="submit" formaction="/edit" style="margin:1%; width:46%">
            Continue Shopping
        </button>
           
        <button class='w3-button w3-green' type="submit" formaction="/checkout" style="margin:1%; width:46%">Check Out</button>
     </div>
     </form>
  </div>

  <!-- End page content -->
</div>


<script>
// Accordion 
function myAccFunc() {
  var x = document.getElementById("demoAcc");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}



// Open and close sidebar
function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}
 
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

function UpdateTotal(id,price) { 
      /* Get prices and calculate total */
      var item_price = price,
          item_count = document.getElementById(id+"_number").value;
      var total = item_price*item_count;


      /* Attempt to update the value (Inside a TD tag) */
  		document.getElementById(id+"_total").innerHTML="$"+total.toFixed(2);
  }


function deleteRow(r) {
  var i = r.parentNode.parentNode.rowIndex;
  document.getElementById("myTable").deleteRow(i);
}

function warn(id){
  var r = confirm("Are you sure leave this page? The system will not store your editing");
  if (r == true) {
    window.location.href = '/detail?id='+id;
  }
}
</script>

</body>
</html>

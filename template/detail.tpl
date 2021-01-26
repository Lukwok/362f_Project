<!DOCTYPE html>
<html>
<title>362fe</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.w3-sidebar a {font-family: "Roboto", sans-serif}
body,h1,h2,h3,h4,h5,h6,.w3-wide {font-family: "Montserrat", sans-serif;}
</style>
<body class="w3-content" style="max-width:1200px">

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-bar-block w3-white w3-collapse w3-top" style="z-index:3;width:250px" id="mySidebar">
  <div class="w3-container w3-display-container w3-padding-16">
    <i onclick="w3_close()" class="fa fa-remove w3-hide-large w3-button w3-display-topright"></i>
    <h3 class="w3-wide"><b>Shopping Mall</b></h3>
  </div>
  <div class="w3-padding-64 w3-large w3-text-grey" style="font-weight:bold">
    <a href="/home" class="w3-button w3-block w3-white w3-left-align">
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
<div class="w3-main" style="margin-left:250px">

  <!-- Push down content on small screens -->
  <div class="w3-hide-large" style="margin-top:83px"></div>
  
  <!-- Top header -->
  <header class="w3-container w3-xlarge">
    <p class="w3-right">
      <i class="fa fa-shopping-cart w3-margin-right"></i>
      <i class="fa fa-search"></i>
    </p>
  </header>


  <div class="w3-container w3-text-grey" id="jeans">
    <br>
  </div>
    <!--table-->
    %for row in rows:
  <div class="w3-container">
    <!--image-->
  	<img class="w3-image" src="data:image/jpeg;base64,{{row[4]}}" alt="photo" width="1500" height="700"> 
    <br><br>
    <form action="" method="POST">
        <table class="w3-table w3-striped">
            <tr><th>Name</th><td>{{row[1]}}</td></tr>
            <tr><th>Price (per 1)</th><td>${{row[2]}}</td></tr>
            <tr><th>Number ({{row[3]}} left)</th>
                %if int(row[3]) > 0:
                  <td><input class="w3-input w3-border" type="number" placeholder="Max: {{row[3]}}" name="number" min=1 max={{row[3]}} required></td>
            </tr>
            <tr><td>
                <button type="submit" formaction="/cart" class="w3-button w3-block w3-green">Add to Cart</button>
              </td>
                %else:
                  <td>Sold Out </td>
            </tr>
            <tr><td></td>     
                %end
            <td>
                <button type="button" class="w3-button w3-block w3-black" onclick="home()">Back</button>
            </td></tr>
        </table>
        <input class="w3-input w3-border" type="hidden" name="id" value="{{row[0]}}">
        <input class="w3-input w3-border" type="hidden" name="price" value="{{row[2]}}">
        <input class="w3-input w3-border" type="hidden" name="name" value="{{row[1]}}">
    </form>
        <br>
  </div>
  %end


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

function home(){
     window.location.href = '/home'
}
</script>

</body>
</html>

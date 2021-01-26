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

<body style="background-color: darkgray">
<!-- !PAGE CONTENT! -->
<header class="w3-container w3-white">
    <h1>362F Project</h1>
</header>
<div class="w3-display-middle" style="width:65%">
	<!--header-->
    <div class="w3-center w3-bar w3-white">
		<h1>Login</h1>
    </div>

    <!-- Form pass to /processlogin-->
    <form action="/logincheck" method="post" class="w3-contaoner w3-card-4">
    <div id="login" class="w3-container w3-white w3-padding-16 myLink">
    <div class="w3-row-padding" style="margin:0 -16px;">
        <p>
          <label>UserName:</label>
          <input name="username" class="w3-input w3-border" type="text" placeholder="Enter your username" required>
        </p>
        <p>
          <label>Password</label>
          <input name="password" class="w3-input w3-border" type="text" placeholder="Enter yout password">
        </p>
    </div>
    </div>
    <!--submit button-->
    <button style="width:100%" class="w3-button w3-dark-grey">Login</button>
    </form>
</div>
</body>
</html
<?php
$servername = "localhost" ;  
$username = "alota227_jose"; 
$pass = "champion"; 

$con = ($GLOBALS["___mysqli_ston"] = mysqli_connect($servername, $username, $pass)) or die("Problem occur in connection");  

$db = ((bool)mysqli_query($con, "USE " . alota227_dallasDB));  
?>


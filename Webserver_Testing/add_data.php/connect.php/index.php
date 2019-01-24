<?php
// Connect to MySQL
require_once("connect.php");

    // Prepare the SQL statement
    //  date_default_timezone_set('Europe/Athens');
    // $dateS = date('m/d/Y h:i:s', time());
    //echo $dateS;
$query = "INSERT INTO alota227_dallasDB.tempdata (Datetime,Temperature) VALUES ('".$_GET["dt"]."','".$_GET["temp"]."')";     

    // Execute SQL statement
    //mysql_query($SQL);
$result = mysqli_query($GLOBALS["___mysqli_ston"], $query);  
    
if(isset($result)) 

{ 

echo "Data has been inserted";  

} 

    // Go to the review_data.php (optional)
    //header("Location: index.php");
?>

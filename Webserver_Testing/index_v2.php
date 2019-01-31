<?php 
    // Start MySQL Connection
require_once("connect.php"); 

?>

<html>
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.js"></script>
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/series-label.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.13/moment-timezone-with-data-2012-2022.min.js"></script>
	<script src= "https://cdn.zingchart.com/zingchart.min.js"></script>
	<script> zingchart.MODULESDIR = "https://cdn.zingchart.com/modules/";
	ZC.LICENSE = ["569d52cefae586f634c54f86dc99e6a9","ee6b7db5b51705a13dc2339db3edaf6d"];</script>    
	
    <title>Raspberry Pi Weather Log</title>
    <style type="text/css">
        .table_titles, .table_cells_odd, .table_cells_even {
                padding-right: 20px;
                padding-left: 20px;
                color: #000;
        }
        .table_titles {
          background-color: #4CAF50;
          color: white;
        }
        .table_cells_odd {
            background-color: #CCC;
        }
        .table_cells_even {
            background-color: #FAFAFA;
        }
        table {
            border: 2px solid #333;
        }
        body { font-family: "Trebuchet MS", Arial; }
        th,td,tr {
        text-align: center;
        }
        h1 {
        color: red;
        font-size: 30px;
        }
        #tableContainer-2 {
             vertical-align: middle;
             display: table-cell;
             width: 100%;
             height: 50%;
             display: table;
        }

         #myTable {
            margin: 0 auto;
        }   
        
    </style>
</head>

    <body>
        <h1 class="text-center">RaspberryPi Temperature Log</h1>
     <div id="tableContainer-2">
        <table id="myTable" border>
            <tr>
                 <td class="table_titles">Date and Time</td>
                 <td class="table_titles">Temperature (C)</td>
            </tr>
<?php

    $query = "select * from tempdata order by Datetime ASC";  
    $result = mysqli_query($GLOBALS["___mysqli_ston"], $query);  

    // Used for row color toggle
    $oddrow = true;

    while($data = mysqli_fetch_array($result)) 
    {
        
       //$dateT[$index]=$data["Datetime"].format("YYYY-MM-DD");
        
        if ($oddrow) 
            { 
                $css_class=' class="table_cells_odd"'; 
            }
        else
            { 
                $css_class=' class="table_cells_even"'; 
            }

        $oddrow = !$oddrow;

        echo '<tr>';
        echo '   <td'.$css_class.'>'.$data["Datetime"].'</td>';
        echo '   <td'.$css_class.'>'.$data["Temperature"].'</td>';
        echo '</tr>';
       //echo json_encode($dateT, JSON_NUMERIC_CHECK);
       // $tempT[$index]=$data["Temperature"];
       //$index++;
    }
?>

        </table>
    </div>  
 <div id='myChart'> </div>

 <div id="tableContainer-2">
        <table id="myTable" border>
            <tr>
                 <td class="table_titles">Average</td>
                 <td class="table_titles">Max</td>
                 <td class="table_titles">Min</td>
            </tr>
<?php
    $sql = "SELECT TRUNCATE(AVG(Temperature),1) FROM tempdata";
    $average = mysqli_query($con, $sql);

    while($avg = mysqli_fetch_array($average)) {
        echo '   <td'.$css_class.'>'.$avg['TRUNCATE(AVG(Temperature),1)'].'</td>';
    }
    
    $sqlmax = "SELECT MAX(Temperature) FROM tempdata";
    $max = mysqli_query($con, $sqlmax);

    while($max_temp = mysqli_fetch_array($max)) {
        echo '   <td'.$css_class.'>'.$max_temp['MAX(Temperature)'].'</td>';
    }
    
    $sqlmin = "SELECT MIN(Temperature) FROM tempdata";
    $min = mysqli_query($con, $sqlmin);

    while($min_temp = mysqli_fetch_array($min)) {
        echo '   <td'.$css_class.'>'.$min_temp['MIN(Temperature)'].'</td>';
    }
    

?>

        </table>
    </div>     
 <?php 
    $query = "select * from tempdata order by Datetime ASC";  
    $result = mysqli_query($GLOBALS["___mysqli_ston"], $query);  

?>   
    <script>
    var myData=[<?php 
    while($data = mysqli_fetch_array($result))
        echo $data['Temperature'].','; /* We use the concatenation operator '.' to add comma delimiters after each data value. */
    ?>];
 <?php 
   
    $query = "select * from tempdata order by Datetime ASC";  
    $result = mysqli_query($GLOBALS["___mysqli_ston"], $query);  

?>  
    var myLabels=[<?php 
    while($data = mysqli_fetch_array($result))
        echo '"'.$data['Datetime'].'",'; /* The concatenation operator '.' is used here to create string values from our database names. */
    ?>];
    </script>
    
    <script>
    window.onload=function(){
    zingchart.render({
    backgroundColor:'#FBFCFE',
    id:"myChart",
    position: 'relative',
    width:"100%",
    height:250,
    data:{
    "type":"bar",
    "title":{
        "text":"Graphical Representation"
    },
    "scale-x":{
        "labels":myLabels
    },
    "series":[
        {
            "values":myData
        }
    ]
    }
    });
    };

    </script>

    </body>
</html>
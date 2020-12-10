<?php

/*
 * Complete the timeConversion function below.
 */
function timeConversion($s) {
    
    $t=substr($s,8,9);
    $c=substr($s,2,6);
    $h=substr($s,0,2);
    
    if($t=='PM'){
       if(intval($h)<12){
            $h=intval($h)+12;
        }
        
    }else{
        if(intval($h)==12){
            $h='00';
        }
    }
    return $h.$c;

}


$s="07:05:45PM";
$result = timeConversion($s);


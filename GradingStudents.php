<?php

/*
 * Complete the 'gradingStudents' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */
function num($base){
    $m=0;
    $m=intdiv($base,5);
        if($m===0){
            $m=1*5;
            
        }else{
            $m=($m+1)*5;
        }
    return $m;
}

function gradingStudents($grades) {
    // Write your code here
    $tam=count($grades);
    $m=[];
    $t=0;
    for ($i=0; $i < $tam; $i++) { 
        $t=num($grades[$i]);
        if(($t-$grades[$i])<3){
            if($t>=40){
                $m[$i]=$t;
            }else{
                $m[$i]=$grades[$i];
            }
            
        }else{
            $m[$i]=$grades[$i];
        }  
    }
    return $m;

}



$grades = array();



$result = gradingStudents($grades);


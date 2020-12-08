<?php

/*
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

function diagonalDifference($arr) {
    // Write your code here
    $tam=count($arr);
    $dp=0;
    $ds=0;
    for ($i=0; $i < $tam; $i++) { 
        $dp+=$arr[$i][$i];
        $ds+=$arr[$i][($tam-1)-$i];
        
    }

}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$n = intval(trim(fgets(STDIN)));

$arr = array();

$arr=[[11,2,4],[4,5,6],[10,8,-12]];

$result = diagonalDifference($arr);

fwrite($fptr, $result . "\n");

fclose($fptr);
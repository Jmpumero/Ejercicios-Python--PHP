<?php

// Complete the miniMaxSum function below.
function miniMaxSum($arr) {

    
    $max=max($arr);
    $min=min($arr);
    $t=array_sum($arr);
   echo ($t-$max)." ".($t-$min);
}

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%[^\n]", $arr_temp);

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));

miniMaxSum($arr);

fclose($stdin);
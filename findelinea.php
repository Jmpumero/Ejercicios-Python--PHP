<?php

// Complete the plusMinus function below.
function plusMinus($arr) {
  $tam=count($arr);
    $positivos=0;
    $negativos=0;
    $ceros=0;
    $tp=0;
    $tn=0;
    $tc=0;
    ini_set('precision', 7);
     for ($i=0; $i < $tam; $i++) { 
       if($arr[$i]>0){
           $positivos++;
       }else{
           if($arr[$i]<0){
                $negativos++;
            }else{
                $ceros++;
            }
       }
    }
    if($positivos>0){
           $tp=$positivos/$tam;
    }
    if($negativos>0){
           $tn=$negativos/$tam;
    }
    if($ceros>0){
           $tc=$ceros/$tam;
    }
    
    
    echo number_format((float) $tp, 6, '.', '').PHP_EOL; // PHP_EOL la gran clave para el fin "salto" de linea
    echo number_format((float) $tn, 6, '.', '').PHP_EOL;
    echo number_format((float) $tc, 6, '.', '').PHP_EOL;
}

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $n);

fscanf($stdin, "%[^\n]", $arr_temp);

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));

plusMinus($arr);

fclose($stdin);
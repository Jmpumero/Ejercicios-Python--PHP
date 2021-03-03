<?php

// Complete the utopianTree function below.
function utopianTree($n) {
    $h=1;
    if ($n==0) {
        return($h); 
    }else {
        for ($i=1; $i <= $n; $i++) { 
            if ($i%2!=0) {
                $h=$h*2;
            }else {
                $h=$h+1;
            }
        }
    }
    return($h);


}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%d\n", $t);

for ($t_itr = 0; $t_itr < $t; $t_itr++) {
    fscanf($stdin, "%d\n", $n);

    $result = utopianTree($n);

    fwrite($fptr, $result . "\n");
}

fclose($stdin);
fclose($fptr);
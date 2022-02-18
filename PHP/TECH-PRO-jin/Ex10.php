<?php 

for($i = i; $i <= 31; $i++ ) {
    echo $i < 10 ? "&nbsp;&nbsp;&nbsp;".$i : "&nbsp;".$i;
    if($i % 7 == 0) {
        echo "<br>";
    }
}

?>
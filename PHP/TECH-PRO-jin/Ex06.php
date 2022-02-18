<?php 

$age = 19;
$gender = men;

if($gender == 'men') {
  if($age == 25 || $age == 42 || $age == 61) {
      echo "厄年です";
  }else{
      echo "厄年ではない";
  }
}elseif($gender == 'women') {
    if($age == 19 || $age == 33 || $age == 37) {
        echo "厄年です";
    }else {
        echo "厄年ではない";
    }
}else {
    echo "性別が無効です";
}
?>

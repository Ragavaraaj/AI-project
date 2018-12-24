<?php

$tamil = $_POST['t'];
$eng = $_POST['e'];
$math = $_POST['m'];
$phy = $_POST['p'];
$chem = $_POST['c'];
$combio = $_POST['cb'];
$total = $_POST['to'];
$data = $tamil . ":" . $eng . ":" . $math . ":" . $phy . ":" . $chem . ":" . $combio . ":" . $total . PHP_EOL;
$fp = fopen("data_sb.txt", "a");
fwrite($fp, $data);
fclose($fp);
//echo "you file is done";
include("thanks.html");
?>
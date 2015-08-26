 <?php
	$input = trim("0000");
echo "\n".$input."\n";

	if(
		str_split($input) == array(0,0,0,0) ||
		strcmp($input, "0000") == 0 ||
		strcmp($input, "000") == 0 ||
		strcmp($input, "00") == 0 ||
		strcmp($input, "0") == 0 ||
		$input === 0 ||
		preg_match("/^[\d]{1,}$/D", $input)
		)echo "Fail\n"; return 0;
                
                if($input == "0000") echo "Success!";
?> 

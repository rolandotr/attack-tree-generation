<?php

//header( 'Content-type: text/html; charset=utf-8' );

//disable_ob();
ob_clean();

$cmd = "ping www.google.com";

$cwd='/tmp';
$descriptorspec = array(
    0 => array("pipe", "r"),
    1 => array("pipe", "w"),
    2 => array("file", "/tmp/error-output.txt", "a") );

$process = proc_open($cmd, $descriptorspec, $pipes, $cwd);

if (is_resource($process))
{

    while( ! feof($pipes[1]))
    {
        $return_message = fgets($pipes[1], 1024);
        if (strlen($return_message) == 0) break;

        echo $return_message.'<br />';
        ob_flush();
        flush();
    }
}

/*echo "<pre>";
system($cmd,$output);
$file=popen($output,'r');
while(fgets($file)!='') {
    echo fgets($file);
    ob_flush();
}

pclose($file);
echo "</pre>";*/

?>

<html>
<head>
    <script type="text/javascript" src="jquery.js"></script>
    <link type="text/css" href="style.css" rel="stylesheet" />
    <link href = "https://code.jquery.com/ui/1.10.4/themes/ui-lightness/jquery-ui.css" rel = "stylesheet">
    <style>
        #myProgress {
            width: 100%;
            background-color: grey;
        }

        #myBar {
            width: 1%;
            height: 30px;
            background-color: green;
        }
    </style>
    <script>
        function move() {
            var elem = document.getElementById("myBar");
            var width = 1;
            var id = setInterval(frame, 10);
            function frame() {
                if (width >= 100) {
                    clearInterval(id);
                } else {
                    width++;
                    elem.style.width = width + '%';
                }
            }
        }
    </script>
</head>
<body>
<!--<div id="loading"></div>-->
<div id="myProgress">
    <div id="myBar"></div>
</div>
<div id="output">
<?php

function progress($progress) {
    echo '<script>$( "#myBar" ).css("width","'.$progress.'%");</script>';
}
    if(isset($_POST['file_submit']) && isset($_POST['upload_style'])) {
        $fileName='phpspecfile'.uniqid().'.mcrl2';
        if(isset($_POST['code_text']) && $_POST['upload_style']=='upload_code') {
            file_put_contents($fileName,$_POST['code_text']);
            echo "File Created successfully<br>";
        }

        if($_POST['upload_style']=='upload_file') {
            //$target_file = basename($_FILES["fileToUpload"]["name"]);
            if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $fileName)) {
                echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded. <br>";
            }
        }

        set_time_limit(300);

        $pyscript="C:/Users/dnagumot/xampp/htdocs/attack_trees/attack-tree-generation/Test/FileParser.py";
        $filePath="C:/Users/dnagumot/xampp/htdocs/attack_trees/attack-tree-generation/".$fileName;
        $cmd = "python $pyscript $filePath";
        //echo "\n $cmd";
        $cwd='/tmp';
        $descriptorspec = array(
            0 => array("pipe", "r"),
            1 => array("pipe", "w"),
            2 => array("file", "/tmp/error-output.txt", "a") );
        echo '<div id="progressbar"></div>';
        echo '<pre>';

        $process = proc_open($cmd, $descriptorspec, $pipes, $cwd);

        if (is_resource($process))
        {

            while( ! feof($pipes[1]))
            {
                $return_message = fgets($pipes[1], 1024);
                if (strpos($return_message, 'Tree Built') !== false) {
                    echo 'Tree Built - 100%<br>';
                    progress(95);
                }
                else if (strpos($return_message, 'Building Tree') !== false) {
                    echo 'Building Tree- 80%<br>';
                    progress(80);

                }
                else if (strpos($return_message, 'trace Parsing') !== false) {
                    echo 'trace Parsing- 63%<br>';
                    progress(63);
                }
                else if (strpos($return_message, 'redundant Traces removed') !== false) {
                    echo 'redundant Traces removed- 60%<br>';
                    progress(60);
                }
                else if (strpos($return_message, 'Traces Generation Done') !== false) {
                    echo 'Traces Generation Done- 50%<br>';
                    progress(50);
                }
                else if (strpos($return_message, 'Trace Generation') !== false) {
                    echo 'Traces Generation - 45%<br>';
                    progress(45);
                }
                else if (strpos($return_message, 'Solving Formula') !== false) {
                    echo 'Solving Formula - 25%<br>';
                    progress(25);
                }
                else if (strpos($return_message, 'Creating Trace-generation Formula') !== false) {
                    echo 'Creating Trace-generation Formula - 12%<br>';
                    progress(12);
                }
                else if (strpos($return_message, 'generating Traces') !== false) {
                    echo '10% - Generating Traces - 10%<br>';
                    progress(10);
            }
                else if (strpos($return_message, 'Mcrl2 parsing') !== false) {
                    echo 'Mcrl2 parsing - 0%<br>';
                    progress(1);
                }
                if (strlen($return_message) == 0) break;

                //echo $return_message.'<br />';
                ob_flush();
                flush();
            }
        }
    }
?>
    </pre>
</div>
<script>
    $(document).ready( function () {
        window.location.href = "output.php";
    });
</script>

</body>
</html>

<html>
<head>
    <script type="text/javascript" src="jquery.js"></script>
    <link type="text/css" href="style.css" rel="stylesheet" />
</head>
<body>
    <div class="content_area">
        <h1>Generation of Attack Trees</h1>
        <div id="mcrl-input">
            <form action="index.php" method="post" id="specification_form">
                <label>Your MCRL2 file</label> <br><br>
                <textarea rows="20" cols="100" name="specification_file" form="specification_form"></textarea> <br><br>
                <input type="submit" name="file_upload" value="Generate Trees" />
            </form>
        </div>
        <div class="output_display">
        <?php
            if(isset($_POST['specification_file']) && isset($_POST['file_upload'])) {

                $fileName='phpspecfile'.uniqid().'.mcrl2';
                file_put_contents($fileName,$_POST['specification_file']);
                echo "File Created successfully";

                $pyscript="C:\\Users\\dnagumot\\xampp\\htdocs\\attack_trees\\Test\\FileParser.py";
                $filePath="C:\\Users\\dnagumot\\xampp\\htdocs\\attack_trees\\".$fileName;
                $cmd = "python $pyscript $filePath";
                //echo $cmd;
                exec("$cmd", $output);
                echo "<div id='images'></div>";
                //var_dump($output);
                echo "<script>$(document).ready( function() { 
                $('#specification_form').hide();
                $('#mcrl-input').append('<button id=\'try-again\' onclick=\'tryAgainClick()\'>Try Again</button>')
                $('#images').append('<h2>Binary Tree</h2>');
                $('#images').append('<img src=\'Test/Bin Tree.gv.png\' style=\'width:500px;height:250px;\' />');
                $('#images').append('<h2>Optimised Tree</h2>');
                $('#images').append('<img src=\'Test/Opt Tree.gv.png\' style=\'width:500px;height:250px;\'/>');    
                }
            )
            function tryAgainClick() {
                    $('#specification_form').show();
                    $('#try-again').remove();
                    $('#images').empty();
                    
            }
            </script>";

            }
        ?>
        </div>
    </div>
</body>
</html>
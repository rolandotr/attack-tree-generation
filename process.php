<html>
<head>
    <script type="text/javascript" src="jquery.js"></script>
    <link type="text/css" href="style.css" rel="stylesheet" />
</head>
<body>
<?php
    if(isset($_POST['file_submit']) && isset($_POST['upload_style'])) {
        $fileName='phpspecfile'.uniqid().'.mcrl2';
        if(isset($_POST['code_text']) && $_POST['upload_style']=='upload_code') {
            file_put_contents($fileName,$_POST['code_text']);
            echo "File Created successfully";
        }

        if($_POST['upload_style']=='upload_file') {
            //$target_file = basename($_FILES["fileToUpload"]["name"]);
            if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $fileName)) {
                echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
            }
        }

        $pyscript="C:/Users/dnagumot/xampp/htdocs/attack_trees/attack-tree-generation/Test/FileParser.py";
        $filePath="C:/Users/dnagumot/xampp/htdocs/attack_trees/attack-tree-generation/".$fileName;
        $cmd = "python $pyscript $filePath";
        echo $cmd;
        exec($cmd, $output);

        echo "<script>
            $(document).ready( function () {
                window.location.href='output.php'
            });
        </script>";
    }
?>

</body>
</html>

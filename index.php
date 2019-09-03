<html>
<head>
    <script type="text/javascript" src="jquery.js"></script>
    <link type="text/css" href="style.css" rel="stylesheet" />
</head>
<body>
    <div class="content_area">
        <h1>Generation of Attack Trees</h1>
        <div id="mcrl-input">
            <form action="process.php" method="post" id="specification_form" enctype="multipart/form-data">
                <label>Your MCRL2 file</label> <br><br>
                <input type="radio" name="upload_style" value="upload_file" id="file_upload" onchange="change_input()"/>Upload File (or)
                <input type="radio" name="upload_style" value="upload_code" id="code_upload" checked onchange="change_input()"/>Enter your MRCL2 code here <br><br>
                <textarea rows="20" cols="100" name="code_text" form="specification_form" id="code_area"></textarea> <br><br>
                <input type="file" name="fileToUpload" id="fileToUpload" /><br><br>
                <input type="submit" name="file_submit" value="Generate Trees" />
            </form>
        </div>
        <script type="text/javascript">
            $("#fileToUpload").hide();
            function change_input() {
                var radioValue = $("input[name='upload_style']:checked").val();
                //console.log(radioValue);
                if (radioValue=="upload_code") {
                    $("#code_area").show();
                    $("#fileToUpload").hide();
                }
                else {
                    $("#code_area").hide();
                    $("#fileToUpload").show();

                }

            }
        </script>

    </div>
</body>
</html>
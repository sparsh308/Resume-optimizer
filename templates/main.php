<?php
$username = $_POST['username'];
$email = $_POST['email'];
if (!empty($username) || !empty($email) ){
 $host = "localhost";
    $dbUsername = "root";
    $dbPassword = "";
    $dbname = "resume_free_users";
    //create connection
    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);
    if (mysqli_connect_error()) {
     die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
    } 
else{
  $sql="INSERT INTO users_info(username,email)values ('$username','$email')";
  if($conn->query($sql)){
    header("location:main.html");
  }
  else
  {
    echo "fail";
  }
}

  }
 else {
 echo "All field are required";
 die();
}
?>



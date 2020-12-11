<?php

  $email = firstName = lastName = streetAddress = city = state = zipCode = phone = "";
  function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
  }

  if ($_SERVER["REQUEST_METHOD"] == "POST") {    
//    $firstName = test_input($_POST["firstName"]);
//    $lastName = test_input($_POST["lastName"]);
//    $email = test_input($_POST["email"]);
//    $streeAddress = test_input($_POST["streeAddress"]);
//    $city = test_input($_POST["city"]);
//    $state = test_input($_POST["state"]);
//    $zipCode = test_input($_POST["zipCode"]);
//    $phone = test_input($_POST["phone"])
//    $msg = "Subscription Request from: " . $firstName . " " . lastName .  ", || email: " . $email . "|| address " . streetAddress ;
//    $msg = $msg . " || City " . $city . " || State " . $state . " || Zip " . $zip;
//    echo "<p>" . $msg . "</p>";
    //mail("molson46@gmail.com","Subscription Request",$msg);
//    echo "<script>";
//    echo "  window.location.href ='./subscriptionRequestResponse.html' ";
//    echo " </script> ";
  }
?>
    

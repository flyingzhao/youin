<?php
	$ip=$_POST['ip'];
	$raspberryid=$_POST['raspberryid'];
	echo "<p>$ip</p>";
	echo "<p>$raspberryid</p>";

	$db=new mysqli('localhost','pi','raspberry','piip');
	$query="update iplist set ip='".$ip."' where id=".$raspberryid;
	$db->query($query);
	$db->close();

	

?>
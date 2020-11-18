<html>
<title>Free Pings</title>
<body>
<form method=GET>
Enter IP: <input type=text name=ip>
<input type=submit>
</form>
<pre>

<?php
if($_GET['ip'])
{
	if(preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\z/m',$_GET['ip'])){
		if(strpos($_GET['ip'], 'flag') !== false)
		{
			echo("Not so fast...");
			die();
		}

	system("ping -c 2 -W 1 " . $_GET['ip']);
	}
}

else{
	echo("Invalid IP");
}
?>
</pre>
</body>
</html>

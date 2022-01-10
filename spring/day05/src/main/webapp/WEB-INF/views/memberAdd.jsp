<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<form method="post">
	<p><input type="text" name="userid" placeholder="id(pk)" required autofocus></p>
	<p><input type="password" name="userpw" placeholder="pwd" required></p>
	<p><input type="text" name="username" placeholder="name" required></p>
	<p><input type="email" name="email" placeholder="foo@bar.com" required></p>
	<p>
		<label><input type="radio" name="gender" value="남성 ">남성</label>
		<label><input type="radio" name="gender" value="여성">여성</label>
	</p>
	<p><input type="submit"></p>
</form>
</body>
</html>
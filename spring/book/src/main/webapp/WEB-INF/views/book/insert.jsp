<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<div>
	<form method="POST">
		<p>name : <input type="text" name="name" required autofocus></p>
		<p>author : <input type="text" name="author" required></p>
		<p>publisher : <input type="text" name="publisher" required></p>
		<p>price : <input type="number" name="price" required></p>
		<p>description<textarea name="description"></textarea></p>
		<p><input type="submit" value="추가">
	</form>
</div>
</body>
</html>
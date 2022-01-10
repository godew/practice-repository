<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>result = ${res }</h2>

<form method="POST">
	<input name="prev" value="${param.test }">
	<select name="oper">
		<option value="plus">+</option>
		<option value="minus">-</option>
		<option value="mul">*</option>
		<option value="div">/</option>
	</select>
	<input name="next" value="${param.test }">
	<input name="test">
	<input type="submit" value="calc">
</form>
</body>
</html>
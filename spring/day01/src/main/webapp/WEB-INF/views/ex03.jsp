<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>ex03</h1>
<hr>

<form method="POST">
	<input type="text" name="name" placeholder="name" required autofocus>
	<input type="number" name="age" placeholder="age" required>
	<input type="submit" value="제출">
</form>
</body>
</html>
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
<h1>회원가입 정보 입력</h1>
<hr>
<form method="post" action="${cpath }/join/step3">
	<p><input type="text" name="userid" placeholder="id" required autofocus></p>
	<p><input type="password" name="userpw" placeholder="password" required></p>
	<p><input type="text" name="username" placeholder="name" required></p>
	<p><input type="email" name="email" placeholder="foo@bar.com" required></p>
	<p>		
		<label><input type="radio" name="gender" value="남성" required>남성</label>
		<label><input type="radio" name="gender" value="여성" required>여성</label>
	</p>
	<p><input type="submit" value="join"></p>
</form>

</body>
</html>
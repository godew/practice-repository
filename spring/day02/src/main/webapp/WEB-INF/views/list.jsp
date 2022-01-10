<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<table border=1 style="border-collapse: collapse;">
<tr style="background-color: orange">
	<th>userid</th>
	<th>userpw</th>
	<th>username</th>
	<th>email</th>
	<th>gender</th>
</tr>
<c:forEach var="member" items="${list }">
	<tr>
		<td>${member.userid }</td>
		<td>${member.userpw }</td>
		<td>${member.username }</td>
		<td>${member.email }</td>
		<td>${member.gender }</td>
	</tr>
</c:forEach>
</table>
</body>
</html>
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
<h1>controller example</h1>
<hr>
<ul>
	<li><a href="${cpath }/ex01">ex01</a></li>
	<li><a href="${cpath }/ex02">ex02</a></li>
	<li><a href="${cpath }/ex03">ex03</a></li>
	<li><a href="${cpath }/ex04">ex04</a></li>
	<li><a href="${cpath }/ex05">ex05</a></li>
	<li><a href="${cpath }/calc">calc</a></li>
</ul>
</body>
</html>
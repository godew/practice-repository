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
<h1>jdbcTemplate test</h1>
<div class="info">
	<div>${login.userid }</div>
</div>
<hr>
<h3>${msg }</h3>

<ul>
	<li><a href="${cpath }/join">join</a></li>
	<li><a href="${cpath }/list">list</a></li>
	<c:if test="${empty login }">
		<li><a href="${cpath }/login">login</a></li>
	</c:if>
	<c:if test="${not empty login }">
		<li><a href="${cpath }/logout">logout</a></li>
	</c:if>
</ul>
</body>
</html>
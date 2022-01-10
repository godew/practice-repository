<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" type="text/css" href="${cpath }/resources/css/style.css">
</head>
<body>
	<header>
		<h1><a href="${cpath }">day08</a></h1>
		<div>
			<c:if test="${not empty login }">
				<a href="${cpath }/memberInfo">memberInfo : ${login.userid }(${login.username })</a>
			</c:if>
		</div>
		<nav>
			<ul>
				<c:if test="${empty login }">
					<li><a class="btn" href="${cpath }/login">로그인</a></li>
				</c:if>
				<c:if test="${not empty login }">
					<li><a class="btn" href="${cpath }/logout">로그아웃</a></li>
				</c:if>
				<li><a class="btn" href="${cpath }/bookList/idx">도서 관리</a></li>
			</ul>
		</nav>
	</header>
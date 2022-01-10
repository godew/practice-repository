<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	body {
		width: 100%;
		overflow-x : hidden;
	}
	nav > ul {
		display: flex;
		padding-left: 0;
		list-style: none;
		width: 800px;
		justify-content: center;
	}
	nav > ul > li {
		width: 100px;
		height: 40px;
		display: flex;
		justify-content: center;
		align-items: center;
		border: 1px solid gray;
		border-right: 0;
	}
	nav > ul > li:last-child {
		border-right: 1px solid black;
	}
	nav > ul > li > a {
		text-decoration: none;
		display: block;
		background-color: black;
		color: white;
		width: 100%;
		height: 100%;
		text-align: center;
		line-height: 40px;
		font-weight: bold;
	}
}
</style>
</head>
<body>
<h1>myBatis test</h1>
<nav>
	<ul>
		<c:if test="${empty login}">
			<li><a href="${cpath }/login">로그인</a></li>
		</c:if>
		<c:if test="${not empty login}">
			<li><a href="${cpath }/logout">로그아웃</a></li>
		</c:if>
		<li><a href="${cpath }/bookList">목록</a></li>
		<li><a href="${cpath }/insert">추가</a></li>
	</ul>
</nav>
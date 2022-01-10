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
		overflow-x: hidden;	
		max-width: 1024px;
		margin: 0 auto;
	}
	div, span, header, nav, main, section, article, footer, aside {
		box-sizing: border-box;
	}
	a {
		text-decoration: none;
		color: inherit;
	}
	a:hover {
		text-decoration: underline;
	}
	.btn {
		display: block;
		width: 100px; height: 40px; line-height: 40px; text-align: center;
		background-color: skyblue;
		color: white;
		font-size: 17px;
		font-weight: bold;
		transition-duration: 1s;
	}
	.btn:hover {
		background-color: blue;
		color: white;
		transition-duration: 0.5s;
		text-decoration: none;
	}
	nav > ul { 
		display: flex;
		justify-content: center;
		list-style: none;
		padding: 0;
	}
	h1 {
		display: flex;
		justify-content: center;
	}
	header > div {
		display: flex;
		justify-content: flex-end;
	}
	header > div > a {
		font-weight: bold;
	}
	.book th {
		cursor: pointer;
	}
	.book th:hover {
		background-color: skyblue;
		color: white;
		cursor: pointer;
	}
</style>
</head>
<body>
	<header>
		<h1><a href="${cpath }">day07</a></h1>
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
</body>
</html>
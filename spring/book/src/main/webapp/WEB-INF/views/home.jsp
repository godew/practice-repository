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
<h1>BOOK</h1>
<div>
	<ul>
		<c:if test="${empty login }">
			<li><a href="${cpath }/login">로그인</a></li>
		</c:if>
		<c:if test="${not empty login }">
			<c:if test="${login.userid eq 'admin' }">
				<li><a href="${cpath }/insert">추가</a></li>
			</c:if>
			<li><a href="${cpath }/logout">로그아웃</a></li>
		</c:if>
		<li><a href="${cpath }/list">목록</a></li>
	</ul>
</div>
</body>
</html>
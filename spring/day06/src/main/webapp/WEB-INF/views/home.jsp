<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>BOOK</h1>
<h3>DB 접속 정보 : ${test }</h3>
<h3>로그인 정보 : ${login.userid }</h3>
<hr>
<ul>
	<li><a href="${cpath }/memberList">회원목록</a></li>
	<c:if test="${empty login }">
		<li><a href="${cpath }/login">로그인</a></li>
	</c:if>
	<c:if test="${not empty login }">
		<li><a href="${cpath }/logout">로그아웃</a></li>
	</c:if>
</ul>
</body>
</html>
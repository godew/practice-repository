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
<ul>
	<li><a href="${cpath }/memberList">회원 목록</a></li>
	<li><a href="${cpath }/memberList/username">회원 목록 - 이름순으로 정렬</a></li>
	<li><a href="${cpath }/memberList/userid">회원 목록 - id순으로 정렬</a></li>
	<li><a href="${cpath }/memberAdd">회원 추가</a></li>
	<li><a href="${cpath }/loginTest">로그인 테스트</a></li>
</ul>
</body>
</html>
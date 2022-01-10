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
<table border="1">
<tr>
	<th>${book.name }</th>
	<th>${book.author }</th>
	<th>${book.price }원</th>
</tr>
<tr>
	<td colspan="3">${book.description }</td>
</tr>
</table>
<div>
	<a href="${cpath }">home</a>
	<c:if test="${login.userid eq 'admin' }">
		<a href="${cpath }/delete?idx=${param.idx }">삭제</a>
		<a href="${cpath }/update?idx=${param.idx }">수정</a>
	</c:if>
</div>
</body>
</html>
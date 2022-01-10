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
<div>
	<form method="POST">
		<p>
			도서명 검색
			<input type="text" name="name" required autofocus>
			<input type="submit" value="검색">
		</p> 
	</form>
</div>
<table border="1">
<tr>
	<th>name</th>
	<th>author</th>
	<th>publisher</th>
	<th>publishDate</th>
</tr>
<c:forEach var="book" items="${books }">
	<tr>
		<td><a href="${cpath }/selectOne?idx=${book.idx }">${book.name }</a></td>
		<td>${book.author }</td>
		<td>${book.publisher }</td>
		<td>${book.publishDate }</td>
	</tr>
</c:forEach>
</table>
<div>
	<a href="${cpath }">home</a>
</div>
</body>
</html>
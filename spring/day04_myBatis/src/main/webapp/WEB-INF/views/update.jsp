<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<div>
	<form method="POST">
		<input type="hidden" name="idx" value="${book.idx }">
		<p>name : <input type="text" name="name" value="${book.name }" required autofocus></p>
		<p>author : <input type="text" name="author" value="${book.author }" required></p>
		<p>publisher : <input type="text" name="publisher" value="${book.publisher }" required></p>
		<p>publishDate : <input type="date" name="publishDate" value="${book.publishDate }" required></p>
		<p>price : <input type="number" name="price" value="${book.price }" required></p>
		<p>description<textarea name="description">${book.description }</textarea></p>
		<p><input type="submit" value="수정">
	</form>
</div>
</body>
</html>
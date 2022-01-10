<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h2>도서 정보 수정: ${book.idx }번 도서</h2>
<form method="post">
	<p><input type="text" name="name" value="${book.name }" required autofocus></p>
	<p><input type="text" name="author" value="${book.author }" required></p>
	<p><input type="text" name="publisher" value="${book.publisher }" required></p>
	<p><input type="date" name="publishDate" value="${book.publishDate }" required></p>
	<p><input type="number" step="1000" name="price" value="${book.price }" required></p>
	<p><textarea name="description">${book.name }</textarea>
	<p><input type="submit" value="modify"></p>
</form>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<form method="post">
	<p><input type="text" name="name" placeholder="name" required autofocus></p>
	<p><input type="text" name="author" placeholder="author" required></p>
	<p><input type="text" name="publisher" placeholder="publisher" required></p>
	<p><input type="date" name="publishDate" placeholder="publishDate" required></p>
	<p><input type="number" step="1000" name="price" placeholder="price" required></p>
	<p><textarea name="description"></textarea>
	<p><input type="submit" value="add"></p>
</form>
</body>
</html>
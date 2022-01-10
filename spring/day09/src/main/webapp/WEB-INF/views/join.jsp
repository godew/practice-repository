<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h2>회원가입</h2>
<form method="post">
	<p><input type="text" name="userid" placeholder="id" required autofocus></p>
	<p><input type="password" name="userpw" placeholder="password" required></p>
	<p><input type="text" name="username" placeholder="name" required></p>
	<p><input type="text" name="email" placeholder="E-mail" required></p>
	<p>
		<label>남성<input type="radio" name="gender" value="남성" required></label>
		<label>여성<input type="radio" name="gender" value="여성" required></label>
	</p>
	<p><input type="submit" value="join"></p>
</form>
</body>
</html>
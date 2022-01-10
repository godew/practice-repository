<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>

<form method="post">
	<p><input type="text" name="userid" placeholder="id" value="${login.userid }" required autofocus readonly></p>
	<p><input type="password" name="userpw" placeholder="password" value="${login.userpw }" required></p>
	<p><input type="text" name="username" placeholder="name" value="${login.username }" required></p>
	<p><input type="text" name="email" placeholder="E-mail" required value="${login.email }"></p>
	<p>
		<label>남성<input type="radio" name="gender" value="남성" required ${login.gender eq "남성" ? "checked" : ""}></label>
		<label>여성<input type="radio" name="gender" value="여성" required ${login.gender eq "여성" ? "checked" : ""}></label>
	</p>
	<p><input type="submit" value="modify"></p>
</form>
</body>
</html>
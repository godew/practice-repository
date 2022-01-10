<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h2>로그인</h2>
<hr>
<form method="post">
	<p><input type="text" name="userid" placeholder="id" required autofocus></p>
	<p><input type="password" name="userpw" placeholder="password" required></p>
	<p><input type="submit" value="login"></p>
</form>

<div class="login">
	<a href="${cpath }/join">아직 회원이 아니십니까?</a>
	<a href="${cpath }/findPw">비밀번호 찾기</a>
</div>
</body>
</html>
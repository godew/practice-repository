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
<h1>ex05 - 경로 변수</h1>
<hr>
<h3>${msg }</h3>

<form>
	<input name="name">
	<input type="submit" value="전송">
</form>

<script>
	var form = document.forms[0]
	
	form.onsubmit = function(event) {
		event.preventDefault()
		var name = form.children[0].value
		alert(name)
		var cpath = '${pageContext.request.contextPath}'
		location.href = cpath + '/ex05/' + name
	}
</script>
</body>
</html>
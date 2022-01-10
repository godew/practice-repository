<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link href="${cpath }/resources/css/style.css" rel="stylesheet">
<script src="${cpath }/resources/js/function.js"></script>
</head>
<body>
<h1><a href="${cpath }">TODO List</a></h1>
<form>
	<p><input name="title" placeholder="title" required autofocus></p>
	<p><input name="content" placeholder="content" required></p>
	<p><input type="date" name="tdate"></p>
	<p><input type="submit"></p>
</form>
<div id="list">
	
</div>
<script>
	const cpath = '${cpath }'
	const form = document.forms[0]
	const list = document.getElementById('list')

	form.onsubmit = submitHandler
	window.onload = loadHandler
	

</script>
</body>
</html>
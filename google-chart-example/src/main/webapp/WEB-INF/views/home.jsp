<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link href="${cpath }/resources/css/style.css" rel="stylesheet">
</head>
<body>
<h1>통합구현 A형</h1>
<div class="name">응시자 : 신은욱</div>
<hr>
<div class="clock"></div>
<div class="result"></div>
<div class="pieChart"></div>
<hr>
<div class="barChart"></div>
<script src="${cpath }/resources/js/function.js"></script>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script>
	const cpath = '${cpath }'
	const clock = document.querySelector('.clock')
	const result = document.querySelector('.result')
	const today = new Date()
	
	let year = today.getFullYear()
	let month = ('0' + (today.getMonth() + 1)).slice(-2);
	let day = ('0' + today.getDate()).slice(-2); 
	
	const date = year + month + day
	
	timer()
	setInterval(timer, 1000)
	renderTable()
	
	window.onload = main
	
</script>
</body>
</html>
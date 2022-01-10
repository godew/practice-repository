<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>공공 데이터 포털 코로나 시도 발생현황</title>
<link href="${cpath }/resources/css/style.css" rel="stylesheet">
</head>
<body>
<h1>공공 데이터 포털 코로나 시도 발생현황</h1>
<hr>
<div id="clock"></div>
<div id="root"></div>
<script src="${cpath }/resources/js/xml2json.js"></script>
<script src="${cpath }/resources/js/function.js"></script>
<script>
	const root = document.getElementById('root')
	const cpath = '${pageContext.request.contextPath }'
	
// 	window.onload = getCovidDataJS
// 	window.onload = getCovidDataJava
	window.addEventListener('load', getCovidDataJava)
	window.addEventListener('load', setInterval(renderClock, 1000))
</script>
</body>
</html>
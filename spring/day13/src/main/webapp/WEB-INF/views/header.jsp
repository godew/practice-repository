<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	header {
		position: fixed;
		width: 100%;
		top: 0;
		left: 0;
		background-color: white;
		z-index: 1;
	}
	
	header + * {
		position: absolute;
		top: 120px;
	}
	.item {
		margin: 140px;
	}
</style>
<script>
	const cpath = '${cpath }'
</script>
</head>
<body>
<header>
	<h1><a href="${cpath }">AJAX fetch</a></h1>
	<hr>
</header>
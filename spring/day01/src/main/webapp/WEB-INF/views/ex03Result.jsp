<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>ex03Result</h1>
<h3>${dto.name }님은 ${dto.age }살이고 ${dto.age >= 20 ? '성인' : '미성년자' }입니다</h3>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<script>
	alert('${msg }')
	if ('${url}' == '') {
		history.go(-1)
	} else {
		location.href = '${pageContext.request.contextPath}/${url}'
	}
</script>
</body>
</html>
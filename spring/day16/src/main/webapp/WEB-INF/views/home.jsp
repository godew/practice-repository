<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>test page</h2>
<script>
	const cpath = '${pageContext.request.contextPath }'
	const url = cpath + '/memberList'
	const opt = {
			method : 'GET'
	}
	
	fetch(url, opt)
		.then(resp => resp.json())
		.then(json => console.log(json))
</script>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>spring file upload</h1>
<hr>
<form method="post" enctype="multipart/form-data">
	<p><input type="text" name="name"></p>
	<p><input type="number" name="age"></p>
	<p><input type="file" name="uploadFile"></p>
	<p><input type="submit" value="전송"></p>
</form>
<%-- <img src="${pageContext.request.contextPath }/upload/${fileName}"> --%>
<img src="file:D:/upload/${fileName }">
<!-- <img src="file:D:/upload/design-ge19f146ac_1920.png"> -->

</body>
</html>
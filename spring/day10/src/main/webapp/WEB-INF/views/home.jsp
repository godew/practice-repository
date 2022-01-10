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
<c:choose>
	<c:when test="${not empty flag}">
		<form method="post" enctype="multipart/form-data">
			<input type="hidden" name="userid" value="${login.userid }">
			<p><input type="file" name="uploadFile"></p>
			<p><input type="submit" value="전송"></p>
		</form>
	</c:when>
	<c:otherwise>
		<div>
			<a href="${cpath }/upload">file upload</a>
		</div>
		<div>
		<c:forEach var="file" items="${files }">
			<a href="${cpath }/upload/${file.changedName}" target="_black">
				<img class="image" src="${cpath }/upload/${file.changedName}" width="100px" height="100px"/>
			</a>
		</c:forEach>
		</div>
	</c:otherwise>
</c:choose>
<script>
// 	let images = document.querySelectorAll('.image')
// 	for(let image of images) {
// 		image.style.transform = 'scale(1)'
// 		image.onclick = function() {
// 			if (image.style.transform == 'scale(1)') {
// 				this.style.transform = 'scale(1.4)'
// 				this.style.zIndex = 1
// 			    this.style.transition = '0.5s';
// 			} else {
// 				this.style.transform = 'scale(1.0)'
// 				this.style.zIndex = 1
// 			    this.style.transition = '0.5s';
// 			}
// 		}
// 	}
</script>
</body>
</html>
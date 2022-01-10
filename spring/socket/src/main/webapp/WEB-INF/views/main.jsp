<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set var="cpath" value="${pageContext.request.contextPath }" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	#textarea {
		width: 400px;
		height: 75vh;
		padding: 10px;
		border: 2px solid black;
		box-sizing: border-box;
		overflow-y: auto;
		background-color: #d5e4ff;
		margin-bottom: 10px;
	}
</style>
</head>
<body>
<script>
	function onMessage(event) {
		let tag = '<div>'
		tag += '<span>' + JSON.parse(event.data).username + '</span>' 
		tag += ' : <span>' + JSON.parse(event.data).message + '</span>'
		tag += '</div>'
		textarea.innerHTML += tag
		// 메시지가 길어지면 자동으로 아래로 스크롤
		textarea.scroll({top: textarea.scrollHeight, behavior: 'smooth'})
	}
	function keyHandler(event) {
		if(event.key == 'Enter') { 
			sendHandler(event)
		}	
	}
	
	function sendHandler(event) {
		const message = send.value
		send.value = ''
		ws.send(JSON.stringify({
			username : username,
			message : message
		}))
		send.focus()
	}
</script>
<c:if test="${empty username }">
	<c:redirect url="/" />
</c:if>
<h1>채팅</h1>
<hr>

<div id="textarea"></div>
<div class="bottom">
	<input id="send" name="send" autofocus>
	<input id="btn" type="button" value="전송">
	<a href="${cpath }/logout"><input type="button" value="나가기"></a>
</div>
<script src="https://cdn.jsdelivr.net/sockjs/1/sockjs.min.js"></script>
<script>
	const cpath = '${cpath}'
	const username = '${username}'
	const btn = document.getElementById('btn')
	const send = document.getElementById('send')
	const textarea = document.getElementById('textarea')
	const ws = new SockJS(cpath + '/chat')
	
	ws.onmessage = onMessage
	ws.onopen = function(msg) {} 
	ws.onclose = function(msg) {}
	ws.onerror = function(msg) {}
	
	btn.onclick = sendHandler
	send.onkeydown = keyHandler
</script>
</body>
</html>
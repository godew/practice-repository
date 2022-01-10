<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<main>
	<h2>AJAX로 POST 형식으로 데이터 전송하기</h2>
	
	<form name="test">
		<p><input name="title" placeholder="title" required autofocus></p>
		<p><input name="writer" placeholder="writer" required></p>
		<p><textarea name="content" placeholder="content"></textarea></p>
		<input text="hidden" name="ipaddr" value="${pageContext.request.remoteAddr }">
		<p><input type="submit" value="작성"></p>
	</form>
</main>
<script>
	const form = document.forms.test
	form.onsubmit = function(event) {
		event.preventDefault()
		let obj = {}
		let formData = new FormData(form)
		
		for(key of formData.keys()) {
			obj[key] = formData.get(key)
		}
		
		const url = cpath + '/board'
		const opt = {
				method: 'POST',
				body: JSON.stringify(obj),
				headers: {
					'Content-Type' : 'application/json; charset=utf-8'
				}
		}
		
		fetch(url, opt)
			.then(resp => resp.text())
			.then(text => {
				if(text == 1) {
					alert('작성 성공')
					location.href = cpath + '/ex01'
				} else {
					alert('작성 실패')
					
				}
			})
	}
</script>
</body>
</html>
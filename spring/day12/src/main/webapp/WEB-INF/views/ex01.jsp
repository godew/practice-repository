<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<script>
	function ajaxHandler(event) {
		const url = cpath + '/ajax1'
		const opt = {
				method : 'GET'
		}
		fetch(url, opt)							// 요청을 만들어 전달하고, 응답을 받는다
			.then(resp => resp.text())			// 응답을 원하는 형태로 변환
			.then(text => res.innerText = text) // 변환된 데이터를 문서에 반영
	}
</script>
<h2>기본 GET 요청</h2>
<button id="btn">요청</button>
<div id="res"></div>

<script>
	const cpath = '${cpath}'
	const btn = document.getElementById('btn')
	const res = document.getElementById('res')
	
	btn.onclick = ajaxHandler
</script>
</body>
</html>
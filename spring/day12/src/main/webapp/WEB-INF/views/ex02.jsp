<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h2>GET, 파라미터 요청</h2>
<input name="char" placeholder="알파벳 한글자를 입력하세요">
<button id="btn">요청</button>
<div id="res"></div>

<script>
	const cpath = '${cpath}'
	const btn = document.getElementById('btn')
	const res = document.getElementById('res')
	
	btn.onclick = function() {
		const ch = document.querySelector('input[name="char"]').value
		const url = cpath + '/ajax2?ch=' + ch
		const opt = {
				method : 'GET'
		}
		fetch(url, opt)							
			.then(resp => resp.text())
			.then(text => res.innerText = ch + '의 ASCII Code : ' + text)			
	}
</script>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h2>member 검색(id로 검색)</h2>
<form name="search">
	<input name="userid" placeholder="검색할 ID 입력">
	<input type="submit" value="검색">
</form>
<div id="res"></div>

<script>
	const form = document.forms.search
	const res = document.getElementById('res')
	const cpath = '${cpath }'
	
	form.onsubmit = function(event) {
		event.preventDefault()
		const userid = form.userid
		
		const url = cpath + '/ajax3?userid=' + userid.value
		const opt = {
			method : 'GET'
		}

		fetch(url, opt)
			.then(resp => resp.json()) // 응답 데이터는 JSON형식의 문자열이므로 JSON객체로 변환하여 처리(객체 -> 문자열 -> json)
			.then(function(json) {
				console.log(json)
				const ul = document.createElement('ul')
				for(let key in json) {
					const li = document.createElement('li')
					li.innerText = key + " : " + json[key]
					ul.appendChild(li)
				}
				res.innerHTML = ''
				res.appendChild(ul)
			})
	}
</script>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<script src="${cpath }/resources/js/ex05.js"></script>

<form name="search">
	<input type="text" name="username" placeholder="사용자이름으로 검색">
	<input type="submit" value="검색">
</form>
<div id="res"></div>

<script>
	const cpath = '${cpath }'
	const res = document.getElementById('res')
	const form = document.forms.search
	const opt = {
		method : 'GET'
	}
	
	form.onsubmit = function(event) {
		const url = cpath + '/ajax5?username=' + form.username.value
		event.preventDefault()
		fetch(url, opt)
			.then(resp => resp.json())
			.then(json => render(res, getDom(json)))
	}

		
</script>
</body>
</html>
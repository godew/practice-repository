<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<script src="${cpath }/resources/js/ex04.js"></script>

<h2>member 목록으로 테이블 만들기</h2>
<div id="res"></div>

<script>
	const cpath = '${cpath }'
	const res = document.getElementById('res')
	const url = cpath + '/ajax4'
	const opt = {
		method : 'GET'
	}
	
	window.onload = function() {
		fetch(url, opt)
			.then(resp => resp.json()) // list를 json객체 배열로 자동으로 만들어줌
			.then(json => render(res, getDom(json))) 
			
			
	}
		
</script>
</body>
</html>
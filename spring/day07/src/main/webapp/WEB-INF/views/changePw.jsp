<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h3>비밀번호 : ${member.userpw }</h3>
<div class="changePw">
	<button>비밀번호 랜덤변경</button>
</div>
<script>
	let item = document.querySelector('.changePw > button')
	item.onclick = function() {
		location.href = '${cpath}/changePw?userid=${member.userid}'
	}
</script>

</html>
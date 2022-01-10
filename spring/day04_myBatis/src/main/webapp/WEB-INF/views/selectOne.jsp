<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<table border="1">
<tr>
	<th>${book.name }</th>
	<th>${book.author }</th>
	<th>${book.price }원</th>
</tr>
<tr>
	<td colspan="3">${book.description }</td>
</tr>
</table>
<c:if test="${login.userid eq 'admin' }">
	<button class="btn">삭제</button>
	<a href="${cpath }/update/${book.idx }"><button>수정</button></a>
</c:if>
<script>
	document.querySelector('.btn').onclick = function() {
		if(confirm('정말 ${book.idx }번 도서를 삭제하시겠습니까?')) {
			location.href = '${cpath }/delete/${book.idx }'
		}
	}
</script>
</body>
</html>
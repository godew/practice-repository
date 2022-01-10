<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h2>책 목록</h2>

<div>
	<form>
		<select name="">
			<option value="idx">번호로 검색</option>
			<option value="name">도서명으로 검색</option>
			<option value="author">저자명으로 검색</option>
		</select>
		<input type="search" name="word" placeholder="검색어를 입력하세요">
		<input type="submit" value="검색">
	</form>
</div>
<table border="1" class="book">
	<tr>
		<th>idx</th>
		<th>name</th>
		<th>author</th>
		<th>publisher</th>
		<th>publishDate</th>
		<th>price</th>
		<th>description</th>		
	</tr>
	<c:forEach var="book" items="${books }">
		<tr>
			<td>${book.idx }</td>
			<td>${book.name }</td>
			<td>${book.author }</td>
			<td>${book.publisher }</td>
			<td>${book.publishDate }</td>
			<td>${book.price }</td>
			<td>${book.description }</td>
		</tr>
	</c:forEach>
</table>
<script>
	let items = document.querySelectorAll('th')
	for (let item of items) {
		item.onclick = function() {
			location.href = '${cpath}/bookList/' + item.firstChild.nodeValue
		}
	}
	chi
	
</script>
</body>
</html>
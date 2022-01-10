<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h3>book list</h3>
<div>
	<form method="POST">
		<p>
			도서명 검색
			<input type="text" name="name" required autofocus>
			<input type="submit" value="검색">
		</p> 
	</form>
</div>
<table>
	<thead>
		<tr>
			<th>번호</th>
			<th>도서명</th>
			<th>저자</th>
			<th>출판사</th>
			<th>출판일자</th>
		</tr>
	</thead>
	<tbody>
		<c:forEach var="book" items="${books }">
			<tr>
				<td>${book.idx }</td>
				<td><a href="${cpath }/selectOne/${book.idx }">${book.name }</a></td>
				<td>${book.author }</td>
				<td>${book.publisher }</td>
				<td>${book.publishDate }</td>
			</tr>
		</c:forEach>
	</tbody>
</table>
</body>
</html>
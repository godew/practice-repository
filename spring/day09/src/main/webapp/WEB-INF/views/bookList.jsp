<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<h2>책 목록</h2>

<div class="column_and_add">
	<form>
		<select name="column">
			<option value="idx">번호로 검색</option>
			<option value="name">도서명으로 검색</option>
			<option value="author">저자명으로 검색</option>
		</select>
		<input type="search" name="search" placeholder="검색어를 입력하세요">
		<input type="submit" value="검색">
	</form>
	<a class="btn" href="${cpath }/addBook">추가</a>
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
		<th style="pointer-events: none;">수정</th>
		<th style="pointer-events: none;">삭제</th>		
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
			<td><button data-idx="${book.idx}" class="modifyBtn">수정</button></td>
			<td><button data-idx="${book.idx}" class="deleteBtn">삭제</button></td>
		</tr>
	</c:forEach>
</table>
<script>
	let cpath = '${cpath}'
	let items = document.querySelectorAll('th')
	let modifyBtns = document.querySelectorAll('.modifyBtn')
	let deleteBtns = document.querySelectorAll('.deleteBtn')
	
	for (let item of items) {
		item.onclick = function() {
			location.href = cpath + '/bookList/' + item.firstChild.nodeValue
		}
	}
	
	deleteBtns.forEach(function(btn) {
		btn.onclick = function() {
			const idx = this.dataset.idx
			if(confirm(idx + '번 도서를 삭제하시겠습니까?') ) {
				location.href = cpath + '/deleteBook/' + idx
			}
		}
	})
	
	for (let btn of modifyBtns) {
		btn.onclick = function() {
			const idx = this.dataset.idx
			location.href = cpath + '/modifyBook/' + idx
		}
	}
</script>
</body>
</html>
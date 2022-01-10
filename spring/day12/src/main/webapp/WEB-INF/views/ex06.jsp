<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<form name="join">
	<p>
		<input type="text" name="userid" placeholder="ID">
		<input type="button" name="valid" value="중복 확인">
	</p>
	<p><input type="password" name="userpw" placeholder="Password"></p>
	<p><input type="text" name="username" placeholder="Username"></p>
	<p><input type="email" name="email" placeholder="Email"></p>
	<p>
		<label><input type="radio" name="gender" value="man">남성</label>
		<label><input type="radio" name="gender" value="woman">여성</label>
	</p>
	<p><input type="submit" value="join"></p>
</form>
<script>
	let form = document.forms.join
	const cpath = '${cpath}'
	form.valid.onclick = function() {
		const url = cpath + '/valid?userid=' + form.userid.value 
		const opt = {
				method : 'GET'
		}
		fetch(url, opt)
			.then(resp => resp.text())
			.then(text => {
				if(text == 'false') {
					alert('중복되는 id가 있습니다.')
					form.userid.select()
				} else {
					alert('사용할 수 있는 id입니다.')
					form.userpw.focus()
				}
			})
	}
</script>
</body>
</html>
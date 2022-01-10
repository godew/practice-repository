<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	h3 {
		margin: 5px;
	}
	.box {
		width: 400px;
		box-sizing: border-box;
		display: flex;
		flex-flow: column;
		justify-content: center;
		border: 2px solid black;
		border-radius: 10px;
		padding: 10px;
		margin-top: 10px;
	}
	.hidden {
		display: none;
	}
	.timer {
		float: right;
	}
</style>
</head>
<body>
<h1>hash, mail</h1>
<hr>
<form name="sendMailForm">
	<div class="box">
		<h3>이메일 주소 입력</h3>
		<div>
			<input type="email" name="email" placeholder="email" required autofocus autocomplete="off">
			<input type="submit" value="인증번호 전송">
		</div>
		<div id="sendMailMsg"></div>
	</div>
</form>

<form name="authMailForm" class="hidden">
	<div class="box">
		<h3>인증 번호 입력</h3>
		<div>
			<input type="text" name="auth" placeholder="인증번호를 입력하세요">
			<input type="submit" value="인증">
		</div>
		<div id="authMailMsg"></div>
		<div class="timer"></div>
	</div>
</form>
<script>
	const sendMailForm = document.forms.sendMailForm
	const sendMailMsg = document.getElementById('sendMailMsg')
	const authMailForm = document.forms.authMailForm
	const authMailMsg = document.getElementById('authMailMsg')
	const cpath = '${pageContext.request.contextPath }'
	const timer = document.querySelector('.timer')
	
	let second
	let interval
	
	function sendMailHandler(event) {
		event.preventDefault()
		
		const email = sendMailForm.email
		const url = cpath + '/mailto/' + email.value + '/'
		const opt = {
			method : 'GET'
		}
		
		fetch(url, opt)
			.then(resp => resp.json())
			.then(json => {
				sendMailMsg.innerText = json.msg
				sendMailMsg.style.color = json.status == 'OK' ? 'blue' : 'red'
				if(json.status == 'OK') {
					authMailForm.classList.remove('hidden')
					authMailForm.auth.focus()
					
					second = 10
					timer.style.color = 'blue'
					authMailMsg.innerText = ''
					timer.innerText = ''
					interval = setInterval(detimer, 1000)
				}
			})
	}
    

    function detimer() {
        let min = Math.floor(second / 60)
        let sec = second % 60 

        if(min < 10) min = '0' + min
        if(sec < 10) sec = '0' + sec

        const format = min + ' : ' + sec
        timer.innerText = format

        if(second <= 0) {
            timer.style.color = 'red'
            clearInterval(interval)
            
       		const url = cpath + '/timeout'
			const opt = {
				method : 'GET'
			}
            
            fetch(url, opt)
        }

        second -= 1
    }
    
	function authMailHandler(event) {
		event.preventDefault()
		
		const auth = authMailForm.auth
		const url = cpath + '/getAuthResult/' + auth.value + '/'
		const opt = {
			method : 'GET'
		}
		fetch(url, opt)
			.then(resp => resp.json())
			.then(json => {
				authMailMsg.innerText = json.msg
				if(json.status == 'OK') {
					authMailMsg.style.color = 'blue'
					clearInterval(interval)
					timer.innerText = ''
				} else {
					authMailMsg.style.color = 'red'
					auth.select()
				}
			})
	}
	sendMailForm.onsubmit = sendMailHandler
	authMailForm.onsubmit = authMailHandler
</script>
</body>
</html>
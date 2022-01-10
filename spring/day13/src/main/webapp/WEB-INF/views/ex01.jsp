<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="header.jsp" %>
<main>

</main>
<script>
	let scrollCnt = 0
	let cnt = 0
	function getBoardData(offset) {
		const url = cpath + '/board/' + cnt
		const opt = {
			method: 'GET'
		}
		
		fetch(url, opt)
			.then(resp => resp.json())
			.then(json => getDom(json))
		
		cnt += 5
	}
	function getDom(json) {
		let dom = ''
		json.forEach(dto => {
			dom += '<div class="item">'
			for(let key in dto) {
				dom += dto[key]		
			}			
			dom += '</div>'
		})

		render(document.querySelector('main'), dom)
	}
	function render(target, dom) {
		target.innerHTML += dom
	}
	window.onload = function() {
		getBoardData()
	}
	
	document.body.onscroll = function() {
    	console.log(document.documentElement.scrollTop)
    	console.log(document.documentElement.clientHeight)
    	console.log(document.documentElement.scrollHeight)
        if(document.documentElement.scrollTop + document.documentElement.clientHeight == document.documentElement.scrollHeight) {
        	getBoardData()
        }
    }
</script>
</body>
</html>
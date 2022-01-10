function submitHandler(event) {
	event.preventDefault()
	
	const url = cpath + '/todo'
	const obj = {
		title : form.title.value,
		content : form.content.value,
		tdate : form.tdate.value
	}
	const opt = {
			method: 'POST',
			body: JSON.stringify(obj),
			headers: {
				'Content-Type' : 'application/json; charset=utf-8'
			}
	}
	
	fetch(url, opt)
		.then(resp => resp.text())
		.then(text => {
			if(text == 1) {
				list.innerHTML = ''
				loadHandler(event)
			} else {
				alert('삽입 실패')
			}
		})
}

function loadHandler(event) {
	url = cpath + '/todo'
	opt = {
		method : 'GET'
	}
	
	fetch(url, opt)
		.then(resp => resp.json())
		.then(json => {
			json.forEach(dto => {
				dto.tdate = new Date(dto.tdate + 1000 * 9 * 60 * 60).toISOString().split('T')[0]
				render(list, getDom(dto))
			})
		})
}
function getDom(dto) {
	let dom = ''
	dom += '<div class="item">'
	for(let key in dto) {
		if(key != 'idx') {
			dom += '<p>' + dto[key] + '</p>'
		}
	}			
	dom += '<button onclick="delClick(this)" data-title=' + dto.title + ' data-idx=' + dto.idx + '>삭제</button>'
	dom += '</div>'
	return dom
}

function render(target, dom) {
	target.innerHTML += dom
}

function delClick(obj) {
	if(confirm(obj.dataset.title + '를 삭제 하시겠습니까?')) {
		url = cpath + '/todo/' + obj.dataset.idx
		opt = {
			method : 'DELETE'
		}
		
		fetch(url, opt)
			.then(resp => resp.text())
			.then(text => {
				if(text == 1) {
					list.innerHTML = ''
					loadHandler(event)
				} else {
					alert('삭제 실패')
				}
			})
	}
}
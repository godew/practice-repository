function render(target, dom) {
	target.innerHTML = ''
	target.innerHTML = dom
}

function getDom(json) {
	let tag = `<table border="1">`
	tag += `<tr>`
	for(let key in json[0]) {
		tag += `<th>${key}</th>`
	}
	tag += `</tr>`
	
	json.forEach(dto => {
		tag += `<tr>`
		for(let key in dto) {
			const value = dto[key]
			tag += `<td>${value}</td>`
		}
		tag += `</tr>`
	})
	tag += `</table>`
		
	return tag
}
function getDom(arr) {
	let tag = `<table border="1">`
		tag += `<tr style="background-color: black; color: white"><th>gubun</th><th>deathCnt</th><th>incDec</th><th>localOccCnt</th><th>overFlowCnt</th><th>qurRate</th></tr>`
	arr.forEach(e => {
		tag += `<tr>`
		tag += `<td>${e.gubun}</td>`
		tag += `<td>${e.deathCnt}</td>`
		tag += `<td>${e.incDec}</td>`
		tag += `<td>${e.localOccCnt}</td>`
		tag += `<td>${e.overFlowCnt}</td>`
		tag += `<td>${e.qurRate}</td>`
		tag += `</tr>`
	})
	tag += `</table>`
	return tag
}

function getCovidDataJS(event) {
//		const url = cpath + '/covid'
	const url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?' +
		'serviceKey=JbsCM3tPudk4tPQaJsTYcl9m%2FMeFgGkRXk5%2BfKCLCtEuieDsXOHu4MIK5K5dls7xj1Kzt1eVPXa4EvVdhouRJg%3D%3D&' +
		'pageNo=1&' +
		'numOfRows=10&' +
		'startCreateDt=20211229&' +
		'endCreateDt=20211229';
		
	const opt = {
			method : 'GET'
	}
	
	fetch(url, opt)
		.then(resp => resp.text())
		.then(text => {
			const xml2json = new XMLtoJSON()
			const obj = xml2json.fromStr(text)
			const arr = obj.response.body.items.item.map(e => {
				return {
					gubun : e.gubun['#text'],
					deathCnt : e.deathCnt['#text'],
					incDec : e.incDec['#text'],
					localOccCnt : e.localOccCnt['#text'],
					overFlowCnt : e.overFlowCnt['#text'],
					qurRate : e.qurRate['#text']
				}
			})
			const tmp = arr.splice(0, 1)
			const sum = arr.splice(17, 1)
			arr.sort((a,b) => {
				return +a.incDec > +b.incDec ? 1 : -1
			})
			
			arr.push(tmp[0])
			arr.push(sum[0])
			
			console.log(arr)
			
			root.innerHTML = getDom(arr)
		})
}

function getCovidDataJava(event) {
	const url = cpath + '/covid'
	const opt = {
			method : 'GET'
	}
	
	fetch(url, opt)
		.then(resp => resp.json())
		.then(json => {
			const arr = json.response.body.items.item.map(e => {
				return {
					gubun : e.gubun,
					deathCnt : e.deathCnt,
					incDec : e.incDec,
					localOccCnt : e.localOccCnt,
					overFlowCnt : e.overFlowCnt,
					qurRate : e.qurRate
				}
			})
			const tmp = arr.splice(0, 1)
			const sum = arr.splice(17, 1)
			arr.sort((a,b) => {
				return +a.incDec > +b.incDec ? 1 : -1
			})
			
			arr.push(tmp[0])
			arr.push(sum[0])
			
			console.log(arr)
			
			root.innerHTML = getDom(arr)
		})
} 

function renderClock() {
    const clock = new Date()
    const year = clock.getFullYear()
    const month = clock.getMonth() + 1
    const date = clock.getDate()
    let hour = clock.getHours()
    let minute = clock.getMinutes()
    let second = clock.getSeconds()

    if(hour < 10) hour = '0' + hour
    if(minute < 10) minute = '0' + minute
    if(second < 10) second = '0' + second

    document.getElementById('clock').innerHTML = year + '-' + month + '-' + date + ' ' + hour + ':' + minute + ":" + second
}
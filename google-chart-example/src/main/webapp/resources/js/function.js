async function main() {
	
	let midLandFcst = await getMidLandFcst()
	let midTa = await getMidTa()
	
	// 구글 차트
	// Load the Visualization API and the corechart package.
	google.charts.load('current', {'packages':['corechart', 'bar']});

	// Set a callback to run when the Google Visualization API is loaded.
	// PieChart
	google.charts.setOnLoadCallback(drawPieChart)
	
	// BarChart
	google.charts.setOnLoadCallback(drawBarChart)
}

async function getMidLandFcst() {
	const url = cpath + '/midLandFcst?date=' + date 
	const opt = {
			method : 'GET'
	}
	
	await fetch(url, opt)
		.then(resp => resp.json())
		.then(json => {
			const data = json.response.body.items.item[0]
			let dom = ``
			const obj = {
					'맑음' : 'sunny',
					'구름많음' : 'many-cloud',
					'흐림' : 'cloud',
					'흐리고 비' : 'rain'	
			}
			dom += `<tr class="weather">`
			let tmp = data.wf3Am
			dom += `<td class="${obj[tmp]}">3일후 날씨 <b>${tmp}</b></td>`
			tmp = data.wf4Am
			dom += `<td class="${obj[tmp]}">4일후 날씨 <b>${tmp}</b></td>`
			tmp = data.wf5Am
			dom += `<td class="${obj[tmp]}">5일후 날씨 <b>${tmp}</b></td>`
			tmp = data.wf6Am
			dom += `<td class="${obj[tmp]}">6일후 날씨 <b>${tmp}</b></td>`
			tmp = data.wf7Am
			dom += `<td class="${obj[tmp]}">7일후 날씨 <b>${tmp}</b></td>`
			tmp = data.wf8
			dom += `<td class="${obj[tmp]}">8일후 날씨 <b>${tmp}</b></td>`
			tmp = data.wf9
			dom += `<td class="${obj[tmp]}">9일후 날씨 <b>${tmp}</b></td>`
			tmp = data.wf10
			dom += `<td class="${obj[tmp]}">10일후 날씨 <b>${tmp}</b></td>`
			dom += `</tr>`
			
			document.querySelector('.result-table').innerHTML += dom
		})
}


async function getMidTa() {
	const url = cpath + '/midTa?date=' + date 
	const opt = {
			method : 'GET'
	}
	
	await fetch(url, opt)
		.then(resp => resp.json())
		.then(json => {
			const data = json.response.body.items.item[0]
			let dom = ``
			const obj = {
					'0' : 'zero',
					'-1' : 'minus',
					'1' : 'white'
			}
			dom += `<tr class="temper">`
			let tmp = +data.taMin3 < 0 ? -1 : +data.taMin3 == 0 ? 0 : 1
			dom += `<td class="${obj[tmp]}">3일후 기온 <b>${data.taMin3}&deg;C ~ ${data.taMax3}&deg;C</b></td>`
			tmp = +data.taMin4 < 0 ? -1 : +data.taMin4 == 0 ? 0 : 1
			dom += `<td class="${obj[tmp]}">4일후 기온 <b>${data.taMin4}&deg;C ~ ${data.taMax4}&deg;C</b></td>`
			tmp = +data.taMin5 < 0 ? -1 : +data.taMin5 == 0 ? 0 : 1
			dom += `<td class="${obj[tmp]}">5일후 기온 <b>${data.taMin5}&deg;C ~ ${data.taMax5}&deg;C</b></td>`
			tmp = +data.taMin6 < 0 ? -1 : +data.taMin6 == 0 ? 0 : 1
			dom += `<td class="${obj[tmp]}">6일후 기온 <b>${data.taMin6}&deg;C ~ ${data.taMax6}&deg;C</b></td>`
			tmp = +data.taMin7 < 0 ? -1 : +data.taMin7 == 0 ? 0 : 1
			dom += `<td class="${obj[tmp]}">7일후 기온 <b>${data.taMin7}&deg;C ~ ${data.taMax7}&deg;C</b></td>`
			tmp = +data.taMin8 < 0 ? -1 : +data.taMin8 == 0 ? 0 : 1
			dom += `<td class="${obj[tmp]}">8일후 기온 <b>${data.taMin8}&deg;C ~ ${data.taMax8}&deg;C</b></td>`
			tmp = +data.taMin9 < 0 ? -1 : +data.taMin9 == 0 ? 0 : 1
			dom += `<td class="${obj[tmp]}">9일후 기온 <b>${data.taMin9}&deg;C ~ ${data.taMax9}&deg;C</b></td>`
			tmp = +data.taMin10 < 0 ? -1 : +data.taMin10 == 0 ? 0 : 1
			dom += `<td class="${obj[tmp]}">10일후 기온 <b>${data.taMin10}&deg;C ~ ${data.taMax10}&deg;C</b></td>`
			dom += `</tr>`
			
			document.querySelector('.result-table').innerHTML += dom
		})
}

function timer() {
	let today = new Date()
	let year = today.getFullYear()
	let month = (today.getMonth() + 1)
	let day = (today.getDate())
	
	let hours = ('0' + today.getHours()).slice(-2); 
	let minutes = ('0' + today.getMinutes()).slice(-2);
	let seconds = ('0' + today.getSeconds()).slice(-2); 
	
	if (hours < 12) {
		clock.innerText = year + '. ' + month  + '. ' + day + '. ' + '오전 ' + hours + ':' + minutes  + ':' + seconds;
	} else {
		clock.innerText = year + '. ' + month  + '. ' + day + '. ' + '오후 ' + hours + ':' + minutes  + ':' + seconds;
	}
}

function renderTable() {
	let today = new Date()
	let year = today.getFullYear()
	let month = (today.getMonth() + 1)
	let day = (today.getDate())
	
	year + '. ' + month  + '. ' + (day+3) + '. '
	
	let dom = ``
	dom += `<table class="result-table">`
	dom += `<tr>`
	for (let i = 3; i <= 10; i++) { 
		dom += `<td>${year}. ${month}. ${day+i}.</td>`
	}
	dom += `</tr>`
	dom += `</table>`
	result.innerHTML = dom
}

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawPieChart() {

	// Create the data table.
	var data = new google.visualization.DataTable()
	data.addColumn('string', 'weather')
	data.addColumn('number', 'frequency')
	const tds = document.querySelectorAll('.weather > td')
	const obj = {
		'sunny' : 0,
		'many-cloud' : 0,
		'cloud' : 0,
		'rain' : 0
	}
	
  	tds.forEach(td => {
	  	obj[td.classList[0]] += 1
  	})
  	data.addRows([
  		['맑음', obj['sunny']],
    	['구름많음', obj['many-cloud']],
    	['흐리고 비', obj['rain']],
    	['흐림', obj['cloud']],
    ])

  	// Set chart options
  	var options = {'title':'날씨 빈도수',
	  			 	'slices': {0:{color: 'skyblue'}, 1:{color: '#dadada'}, 2:{color: 'grey'}, 3:{color: 'darkgrey'}},
	  			 	'width':400,
	  			 	'height':300}
  
  	// Instantiate and draw our chart, passing in some options.
  	var chart = new google.visualization.PieChart(document.querySelector('.pieChart'))
  	chart.draw(data, options);
}

function drawBarChart() {

	const bs = document.querySelectorAll('.temper > td > b')
	
	let tmp = [['기온', '최저기온', '최고기온']] 
	for (let i = 0; i < 8; i++) {
		tmp.push(
				[(i+3) + '일 후', +bs[i].innerText.split('°C')[0], +bs[i].innerText.split('°C')[1].split(' ')[2]]
		)
	}
	bs.forEach(b => {
		min = +b.innerText.split('°C')[0]
		max = +b.innerText.split('°C')[1].split(' ')[2]
	})
	
	var data = google.visualization.arrayToDataTable(tmp)

	var materialOptions = {
		width: 900,
		chart: {
			title: '최저, 최고기온 그래프',
			subtitle: '왼쪽이 최저기온, 오른쪽이 최고기온'
		}
//		series: {
//			0: { axis: '최저기온' }, // Bind series 0 to an axis named 'min'.
//			1: { axis: '최고기온' } // Bind series 1 to an axis named 'max'.
//		}
//		axes: {
//			y: {
//				min: {label: '최저기온'}, // Left y-axis.
//				max: {side: 'right', label: '최고기온'} // Right y-axis.
//			}
//		}
	}

	var materialChart = new google.charts.Bar(document.querySelector('.barChart'))
	materialChart.draw(data, google.charts.Bar.convertOptions(materialOptions))
}
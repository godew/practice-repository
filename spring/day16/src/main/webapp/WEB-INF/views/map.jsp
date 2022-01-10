<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<div class="nav">
	<ul>
		<li class="list1" style="padding-top: 14px;"><img src="http://www.kyochon.com/images/common/icon_home.png"></li>
		<li class="list1"><a href="">Kyochon home</a></li>
		<li class="list3"><img src="http://www.kyochon.com/images/common/arr_pageNavi.png"></li>
		<li class="list1"><a href="">매장안내</a></li>
		<li class="list2"><img src="http://www.kyochon.com/images/common/icon_pageNavi_link.png"></li>
		<li class="list3"><img src="http://www.kyochon.com/images/common/arr_pageNavi.png"></li>
		<li class="list1"><a href="">국내매장</a></li>
		<li class="list2"><img src="http://www.kyochon.com/images/common/icon_pageNavi_link.png"></li>
	</ul>
</div>
<div class="domestic">
	<h2>국내매장</h2>
	<strong>매장찾기</strong>
	<div class="search">
		<form method="POST">
			<div class="address">
				<select name="first">
					<option value="busan">부산</option>
				</select>
				<select name="second">
					<option value="haeundae">해운대구</option>
				</select>
				<input class="first" type="text" name="name" placeholder="매장명 입력" required>
				<input class="second" type="submit" value="검색">
			</div>
		</form>
	</div>
	<c:set var="mapDao" value="<%= MapDAO.getInstance() %>" />
	<div class="content">
		<div class="scroll">
			<c:choose>
				<c:when test="${pageContext.request.method eq 'POST' }">
					<c:forEach var="mapDto" items="${mapDao.selectByName(param.name) }">
						<div>
							<a href="${cpath }/map/domestic.jsp?address=${mapDto.address }">
								<div class="text1">${mapDto.name }</div>
								<div class="text2">${mapDto.address }</div>
							</a>
						</div>
					</c:forEach>
				</c:when>
				<c:otherwise>
					<c:forEach var="mapDto" items="${mapDao.selectAll() }">
						<div>
							<a href="${cpath }/map/domestic.jsp?address=${mapDto.address }">
								<div class="text1">${mapDto.name }</div>
								<div class="text2">${mapDto.address }</div>
							</a>
						</div>
					</c:forEach>
				</c:otherwise>
			</c:choose>
		</div>
		<div id="map" style="width:1008px; height:528px;"></div>
	</div>
</div>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=14fcfa070d391cfe2e9a41799330572f&libraries=services"></script>
<script>
	var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
	var options = { //지도를 생성할 때 필요한 기본 옵션
		center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
		level: 4 //지도의 레벨(확대, 축소 정도)
	};
	
	var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴
	
	// 마커가 표시될 위치입니다 
	var markerPosition  = new kakao.maps.LatLng(33.450701, 126.570667); 

	// 마커를 생성합니다
	var marker = new kakao.maps.Marker({
	    position: markerPosition
	});

	// 마커가 지도 위에 표시되도록 설정합니다
	marker.setMap(map);  
	
	// 주소-좌표 변환 객체를 생성합니다
	var geocoder = new kakao.maps.services.Geocoder();
	
	// 주소로 좌표를 검색합니다
	geocoder.addressSearch('${param.address }', function(result, status) {
	
	    // 정상적으로 검색이 완료됐으면 
	     if (status === kakao.maps.services.Status.OK) {
	
	        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
	
	        // 결과값으로 받은 위치를 마커로 표시합니다
	        var marker = new kakao.maps.Marker({
	            map: map,
	            position: coords
	        });
	
	        // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
	        map.setCenter(coords);
	        map.setLevel(3);
	    } 
	});    

</script>
<%@ include file="../footer.jsp" %>
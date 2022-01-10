package com.wedog.service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.controller.ImageDTO;
import com.wedog.controller.ItemDTO;
import com.wedog.controller.ItemRoomDTO;
import com.wedog.repository.CrawlingDAO;

@Service
public class Crawling {

	@Autowired CrawlingDAO dao;

	public void start() throws IOException {
		// calendar
		for (int i = 0; i < 1705 * 3; i++) {
			dao.insertCalendar(i / 3 + 1);
		}
//		ArrayList<ItemDTO> itemList = new ArrayList<>();
//		ArrayList<ItemRoomDTO> itemRoomList = new ArrayList<>();
//		ArrayList<ImageDTO> imageList = new ArrayList<>();
//		int cnt = 1;
//		int cnt2 = 1;
//		
//
//		int[] areacode = {5001, 5002, 5003, 5004, 5005};
//		for (int n : areacode) {		
//			String url = "https://www.goodchoice.kr/product/search/5/" + n;
//			Document document = Jsoup.connect(url).get();
//			
//			
//			// =================================ItemDTO
//			Elements elements = document.select(".adcno5");
//			for (Element element : elements) {
//				ItemDTO item = new ItemDTO();
//				item.setItemId(cnt); // Itemid
//				item.setAreaCode(n); // areacode
//				item.setItemName(element.select("strong").text()); // itemName
//				item.setLocale(element.select(".name > p:nth-child(3)").text()); // locale
//				
//				String tmp = element.select(".map_html b:nth-child(2)").text();
//				tmp = tmp.isEmpty() ? element.select(".map_html b").text() : tmp;
//				tmp = tmp.substring(0, tmp.length()-1);
//				int price = Integer.valueOf(Arrays.stream(tmp.split(",")).reduce((a,b) -> a+b).get());
//				item.setItemPrice(price); // itemPrice
//				
//				item.setItemImage(element.select(".pic img").attr("abs:data-original")); // itemImage
//				
//				String[] tmpArr = element.select("a").attr("abs:data-distance").split("/");
//				item.setDistance(Double.valueOf(tmpArr[tmpArr.length-1])); // distance
//				
//				String[] tmpArr2 = element.select("a").attr("abs:data-alat").split("/");
//				item.setLatitude(Double.valueOf(tmpArr2[tmpArr2.length-1])); // latitude
//				
//				String[] tmpArr3 = element.select("a").attr("abs:data-alng").split("/");
//				item.setLongitude(Double.valueOf(tmpArr3[tmpArr3.length-1])); // longitude
//				
//				
//				/**
//				 * 내부 정보 크롤링
//				 */
//				
//				String inUrl = element.select("a").attr("abs:href").split("&")[0] + "&sel_date=2022-01-22&sel_date2=2022-01-23"; // 내부 url
//				Document inDocument = Jsoup.connect(inUrl).get();
//				
//				item.setAddress(inDocument.select(".address").text()); // address
//				
//				String filter = "";
//				for (Element filterElement : inDocument.select(".theme_wrap > li")) {
//					filter += filterElement.text() + " ";
//				};
//				item.setFilter(filter); // filter
//				
//				
//				itemList.add(item); 
//				
//				// =================================ItemRoomDTO
//				
//				Elements inElements = inDocument.select(".room");
//				Elements pElements = inDocument.select(".pop_useinfo");
//				
//				for (int i = 0; i < inElements.size(); i++, cnt2++) {
//					
//					// **가격이 없으면 데이터 안넣음**
//					ItemRoomDTO itemRoom;
//					String inTmp = inElements.get(i).select(".price b").text();
//					if(!inTmp.isEmpty()) {
//						itemRoom = new ItemRoomDTO();
//						int inPrice = Integer.valueOf(Arrays.stream(inTmp.substring(0, inTmp.length()-1).split(",")).reduce((a,b) -> a+b).get());
//						itemRoom.setItemRoomPrice(inPrice); // itemRoomPrice
//					} else {
//						cnt2--;
//						continue;
//					}
//					
//					itemRoom.setItemId(cnt); // itemId
//					itemRoom.setItemRoomId(cnt2); // itemRoomId
//					
//					itemRoom.setItemRoomImage(inElements.get(i).select(".pic_view img").attr("abs:data-original")); // itemRoomImage
//					itemRoom.setItemRoomName(inElements.get(i).select(".title").text()); // itemRoomName
//					
//					// ================================= ImageDTO
//					Elements image = inElements.get(i).select(".item .owl-lazy");
//					for (Element e: image) {
//						ImageDTO imageDto = new ImageDTO();
//						imageDto.setItemRoomId(cnt2); // itemRoomId
//						imageDto.setImage(e.attr("abs:data-src")); // image
//						imageList.add(imageDto);
//					} 
//					// =====================================
//					
//					
//					String people;
//					if (pElements.get(i).select(".scroller > section").get(0).select("li").get(0).text().length() > 22) {
//						people = pElements.get(i).select(".scroller > section").get(1).select("li").get(0).text();
//					} else {
//						people = pElements.get(i).select(".scroller > section").get(0).select("li").get(0).text();
//					}
//					itemRoom.setStandardPeople(people.split("인")[0]); // standardPeople
//					itemRoom.setMaxPeople(people.split("인")[1].split(" ")[3]); // maxPeople
//					
//					itemRoomList.add(itemRoom); 
//				}
//				
//				cnt++;
//				System.out.println("=====");
//			}
//		}
//		for (ItemDTO tmp : itemList) {
//			dao.insertToItem(tmp);
//		}
//		for (ItemRoomDTO tmp : itemRoomList) {
//			dao.insertToItemRoom(tmp);
//		}
//		for (ImageDTO tmp : imageList) {
//			dao.insertToImage(tmp);
//		}
//		System.out.println(itemList.size());
//		System.out.println(itemRoomList.size());
//		System.out.println(imageList.size());
//		System.out.println(cnt);
//		System.out.println(cnt2);
	}
}

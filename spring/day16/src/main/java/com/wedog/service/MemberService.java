package com.wedog.service;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

import org.springframework.stereotype.Service;

@Service
public class MemberService {

	public String getMemberList() throws IOException {
	 	String url = "http://221.164.9.200/memberList";
	 	URL requestURL = new URL(url);
	 	HttpURLConnection conn = (HttpURLConnection) requestURL.openConnection();
	 	conn.setRequestMethod("GET");
	 	conn.setRequestProperty("Content-Type", "application/json; charset=utf-8");
	 	
	 	Scanner sc = null;
	 	String json = "";
	 	
	 	if(conn.getResponseCode() == 200) { // 요청 결과 응답이 200 OK 이면
	 		sc = new Scanner(conn.getInputStream());
	 		while(sc.hasNextLine()) {
	 			json += sc.nextLine();
	 		}
	 		sc.close();
	 		conn.disconnect();
	 		return json;
	 	}
		return null;
	}
}

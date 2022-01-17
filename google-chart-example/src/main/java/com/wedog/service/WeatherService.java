package com.wedog.service;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

import org.springframework.stereotype.Service;

@Service
public class WeatherService {

	private final String url1 = "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst";
	private final String url2 = "http://apis.data.go.kr/1360000/MidFcstInfoService/getMidTa";
	private final String serviceKey = "JbsCM3tPudk4tPQaJsTYcl9m%2FMeFgGkRXk5%2BfKCLCtEuieDsXOHu4MIK5K5dls7xj1Kzt1eVPXa4EvVdhouRJg%3D%3D";
	
	public String getMidLandFcst(String date) throws IOException {        
        
		String queryString = "?";
		queryString += "serviceKey=" + serviceKey + "&";
		queryString += "pageNo=" + 1 + "&";
		queryString += "numOfRows=" + 10 + "&";
		queryString += "dataType=" + "json" + "&";
		queryString += "regId=" + "11H20000" + "&";
		queryString += "tmFc=" + date + "0600" + "&";
		
		URL requestURL = new URL(url1 + queryString);
		HttpURLConnection conn = (HttpURLConnection) requestURL.openConnection();
		conn.setRequestMethod("GET");
		conn.setRequestProperty("Content-Type", "application/json; charset=utf-8");
		
		Scanner sc = null;
		String data = "";
		
		if(conn.getResponseCode() == 200) {
			sc = new Scanner(conn.getInputStream());
			while(sc.hasNextLine()) {
				data += sc.nextLine();
			}
			sc.close();
		}
		
		conn.disconnect();
		return data;
	}
	
	public String getMidTa(String date) throws IOException {        
        
		String queryString = "?";
		queryString += "serviceKey=" + serviceKey + "&";
		queryString += "pageNo=" + 1 + "&";
		queryString += "numOfRows=" + 10 + "&";
		queryString += "dataType=" + "json" + "&";
		queryString += "regId=" + "11H20201" + "&";
		queryString += "tmFc=" + date + "0600" + "&";
		
		URL requestURL = new URL(url2 + queryString);
		HttpURLConnection conn = (HttpURLConnection) requestURL.openConnection();
		conn.setRequestMethod("GET");
		conn.setRequestProperty("Content-Type", "application/json; charset=utf-8");
		
		Scanner sc = null;
		String data = "";
		
		if(conn.getResponseCode() == 200) {
			sc = new Scanner(conn.getInputStream());
			while(sc.hasNextLine()) {
				data += sc.nextLine();
			}
			sc.close();
		}
		
		conn.disconnect();
		return data;
	}

}



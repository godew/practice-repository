package com.wedog.controller;

import java.io.IOException;

import org.json.XML;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.wedog.service.CovidService;

@RestController
public class AjaxController {
	
	@Autowired private CovidService covidService;
	
	@GetMapping(value = "/covid", produces = "application/json; charset=utf-8")
	public String covid() throws IOException {
		
		String xml = covidService.getData();
		if(xml != null) {
			return XML.toJSONObject(xml).toString();
		}
		
		return "{\"msg\" : \"no data\"}";
	}
}

package com.wedog.controller;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.wedog.service.WeatherService;

@Controller
public class HomeController {
	@Autowired private WeatherService weatherService;
	
	@GetMapping("/")
	public String home() {
		return "home";
	}
	
	@GetMapping(value = "/midLandFcst", produces = "application/json; charset=utf-8")
	@ResponseBody
	public String midLandFcst(String date) throws IOException {
		return weatherService.getMidLandFcst(date);
	}
	
	@GetMapping(value = "/midTa", produces = "application/json; charset=utf-8")
	@ResponseBody
	public String midTa(String date) throws IOException {
		return weatherService.getMidTa(date);
	}
}

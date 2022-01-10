package com.wedog.controller;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import com.wedog.service.Crawling;

@Controller
public class HomeController {
	
	@Autowired Crawling crawling;
	
	@RequestMapping("/")
	public String home() throws IOException {
		crawling.start();
		return "home";
	}
}

package com.wedog.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.wedog.service.TestService;

@Controller
public class HomeController {

	@Autowired private TestService service;
	
	@RequestMapping("/")
	public String home(Model model) {
		model.addAttribute("test", service.getTest());
		return "home";
	}
}

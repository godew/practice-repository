package com.wedog.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.wedog.service.TestService;

@Controller
public class HomeController {
	
	@Autowired private TestService ts;
	
	@RequestMapping("/")
	public String home(Model model) {
		String test = ts.getInfo();
		model.addAttribute("test", test);
		return "home";
	}
}

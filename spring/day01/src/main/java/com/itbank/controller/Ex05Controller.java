package com.itbank.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class Ex05Controller {
	
	@GetMapping("/ex05")
	public void ex05() {
		
	}
	
	@GetMapping("/ex05/{name}")
	public ModelAndView ex05(@PathVariable String name) {
		ModelAndView mav = new ModelAndView("ex05");
		mav.addObject("msg", "hello, " + name);
		
		return mav;
	}
}

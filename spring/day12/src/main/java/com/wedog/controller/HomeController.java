package com.wedog.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HomeController {
	
	@RequestMapping("/")
	public String home() {
		return "home";
	}
	
	@GetMapping("ex01")
	public void ex01() {}
	
	@GetMapping("ex02")
	public void ex02() {}
	
	@GetMapping("ex03")
	public void ex03() {}
	
	@GetMapping("ex04")
	public void ex04() {}
	
	@GetMapping("ex05")
	public void ex05() {}
	
	@GetMapping("ex06")
	public void ex06() {}
}

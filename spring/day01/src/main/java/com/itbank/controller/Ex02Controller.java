package com.itbank.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class Ex02Controller {
	
	@GetMapping("/ex02")
	public String ex02() {
		return "ex02";
	}
	
	@PostMapping("/ex02") // 스프링 4.1.0 이상부터 가능
	// @RequestParam : request.getParameter(변수이름) => 생략가능
	public String ex02(@ModelAttribute("name") String name, int age, Model model) {
		model.addAttribute("adult", age >= 20 ? "성인" : "미성년자");
		model.addAttribute("age", age);
		return "ex02Result";
	}
}

package com.itbank.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.itbank.member.MemberDTO;

@Controller
public class Ex03Controller {
	
	@GetMapping("/ex03")
	public void ex03() {
		// 컨트롤러 메서드의 반환형이 void이면 @ReqestMapping의 value가 viewName이 된다
		// => 요청 주소 그대로 jsp를 찾아간다
	}
	
//	@PostMapping("/ex03")
//	public String ex03(@ModelAttribute("dto") MemberDTO dto, Model model) {
//		return "ex03Result";
//	}
	@PostMapping("/ex03")
	public String ex03(@ModelAttribute("dto") MemberDTO dto) {
		return "ex03Result";
	}
}

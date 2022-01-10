package com.itbank.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.member.MemberDTO;

@Controller
public class Ex04Controller {
	
	@GetMapping("/ex04")
	public void ex04() {
		
	}
	
	// 함수의 반환형은 viewName이고, view에게 객체를 전달하기 위해서 Model을 사용한다.
	// 둘다 DispatcherServlet을 통해서 전달하므로, 두 요소를 하나로 묶어서 반환하도록 modelAndView를 사용할 수 있다.
	@PostMapping("/ex04")
	public ModelAndView ex04(MemberDTO dto) {
		ModelAndView mav = new ModelAndView("ex04Result");
		mav.addObject("dto", dto);
		return mav;
	}
}

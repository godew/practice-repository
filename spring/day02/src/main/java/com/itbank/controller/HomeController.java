package com.itbank.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.itbank.service.DBTestService;

@Controller
public class HomeController {
	
	@Autowired // 스프링 빈 중에서 타입이 일치하는 객체를 자동으로 맵핑한다.
	private DBTestService ds;

	@RequestMapping("/")
	public String home(Model model) {
		
		model.addAttribute("msg", ds.getTest());
		return "home";
	}
}

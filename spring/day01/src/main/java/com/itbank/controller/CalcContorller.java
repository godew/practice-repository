package com.itbank.controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.itbank.member.CalcDTO;

@Controller
public class CalcContorller {

	@GetMapping("/calc")
	public String calc() {
		return "calc";
	}
	
	@PostMapping("/calc")
	public String calc(CalcDTO dto, Model model) {
		model.addAttribute("res", dto.calc());
		
		return "calc";
	}
}

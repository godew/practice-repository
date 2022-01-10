package com.wedog.controller;

import java.util.HashMap;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class Ex02Controller {

	@GetMapping("ex02")
	public void ex02() {
		
	}
	
	@GetMapping("ex02Ajax")
	@ResponseBody
	public int ex02Ajax(int n1, int n2) {
		return n1 + n2; 
	}
}

package com.wedog.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class Ex01Controller {
	
	@GetMapping("ex01")
	public void ex01() {
		
	}
	
	@GetMapping("ex01-ajax")
	@ResponseBody // 이 메서드는 응답의 내용을 직접 반환합니다.
	public String ex01Ajax() {
		return "hello, world !!";
	}
}

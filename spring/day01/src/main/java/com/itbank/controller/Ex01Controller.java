package com.itbank.controller;

import java.io.IOException;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class Ex01Controller {
	
	@RequestMapping(value = "/ex01", method = RequestMethod.GET)
	public String ex01() {
		return "ex01";
	}
	
	@RequestMapping(value = "/ex01", method = RequestMethod.POST)
	public String ex01(HttpServletRequest request) throws IOException {
		
		request.setCharacterEncoding("UTF-8");
		String name = request.getParameter("name");
		int age = Integer.parseInt(request.getParameter("age"));
		
		String adult = age >= 20 ? "성인" : "미성년자";
		
		request.setAttribute("name", name);
		request.setAttribute("age", age);
		request.setAttribute("adult", adult);
	
		return "ex01Result";
	}
}

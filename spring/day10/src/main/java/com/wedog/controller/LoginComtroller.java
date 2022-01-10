package com.wedog.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.wedog.model.MemberDTO;
import com.wedog.service.MemberService;

@Controller
public class LoginComtroller {
	
	@Autowired private MemberService memberService;
	
	@GetMapping("login")
	public String login() {
		return "login";
	}
	
	@PostMapping("login")
	public String login(MemberDTO dto, HttpSession session, String url) {
		MemberDTO member = memberService.login(dto);
		session.setAttribute("login", member);
		return "redirect:" + url;
	}
}

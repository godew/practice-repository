package com.wedog.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.wedog.model.MemberDTO;
import com.wedog.service.LoginService;

@Controller
public class LoginController {
	
	@Autowired
	private LoginService ls;
	
	@GetMapping("/login")
	public String login() {
		return "login";
	}
	
	@PostMapping("/login")
	public String login(MemberDTO dto, HttpSession session, Model model) {
		MemberDTO member = ls.login(dto);
		session.setAttribute("login", member);
		if (member == null) {
			model.addAttribute("msg", "로그인 실패. 계정과 비밀번호를 다시 확인해주세요");
			model.addAttribute("url", "/login");
			return "alert";
		}
		return "redirect:/";
	}
	
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/";
	}
}

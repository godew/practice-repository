package com.wedog.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import com.wedog.model.BookDTO;
import com.wedog.model.MemberDTO;
import com.wedog.service.LoginService;

@Controller
public class LoginController {
	
	@Autowired
	private LoginService loginService;
	
	@GetMapping("/")
	public String home() {
		return "home";
	}
	
	@GetMapping("/login")
	public String login() {
		return "login/login";
	}
	
	@PostMapping("/login")
	public String login(MemberDTO dto, HttpSession session) {
		MemberDTO member = loginService.login(dto);
		session.setAttribute("login", member);
		return "redirect:/";
	}
	
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/";
	}
	
	@ExceptionHandler(EmptyResultDataAccessException.class)	// DataAccessException
	public ModelAndView loginFail(EmptyResultDataAccessException e) {
		ModelAndView mav = new ModelAndView("alert");
		mav.addObject("msg", "로그인 실패. 계정과 비밀번호를 다시 확인해주세요");
		mav.addObject("url", "/login");
		return mav;
	}
}

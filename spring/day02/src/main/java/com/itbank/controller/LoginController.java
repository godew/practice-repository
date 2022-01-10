package com.itbank.controller;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.servlet.ModelAndView;

import com.itbank.model.MemberDTO;
import com.itbank.service.MemberService;

@Controller
public class LoginController {
	
	@Autowired
	private MemberService ms;
	
	@GetMapping("/login")
	public void login() {
		
	}
	
	@PostMapping("/login")
	public String login(MemberDTO dto, HttpSession session) {
		MemberDTO login = ms.login(dto);
		session.setAttribute("login", login);
		return "redirect:/";
	}
	
	
	@ExceptionHandler(EmptyResultDataAccessException.class)	// DataAccessException
	public ModelAndView loginFail(EmptyResultDataAccessException e) {
		System.out.println(e);
		ModelAndView mav = new ModelAndView("alert");
		mav.addObject("msg", "로그인 실패. 계정과 비밀번호를 다시 확인해주세요");
		mav.addObject("url", "/day02/login");
		return mav;
	}
	
	@GetMapping("/logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/";
	}
}

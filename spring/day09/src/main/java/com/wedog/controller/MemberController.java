package com.wedog.controller;

import java.util.List;
import java.util.Optional;
import java.util.stream.Stream;

import javax.servlet.http.HttpSession;

import org.apache.ibatis.reflection.ArrayUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DuplicateKeyException;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import com.wedog.member.MemberDTO;
import com.wedog.service.MemberService;

@Controller
public class MemberController {
	
	@Autowired private MemberService service;
	
	@GetMapping("memberList")
	public String memberList(Model model) {
		List<MemberDTO> members = service.getList();
		model.addAttribute("members", members);
		return "memberList";
	}
	
	@GetMapping("login")
	public void login() {
		
	}
	
	@PostMapping("login")
	public String login(MemberDTO dto, HttpSession session, Model model, String url) {
		MemberDTO member = service.login(dto);
		if (member == null) {
			model.addAttribute("url", "login");
			model.addAttribute("msg", "id, pw를 확인하세요");
			return "alert";
		} else {
			session.setAttribute("login", member);
			return url == null ? "redirect:/" : "redirect:" + url;
		}
	}
	
	@GetMapping("logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/";
	}
	
	@GetMapping("join")
	public void join() {
	}
	
	@PostMapping("join")
	public String join(MemberDTO dto, Model model) {
		
		int row = service.join(dto);
		if (row == 1) {
			model.addAttribute("url", "login");
			model.addAttribute("msg", "회원가입 성공");
		}
		return "alert";
	}
	
	@GetMapping("findPw")
	public void findPw() {
	}
	
	@PostMapping("findPw")
	public String findPw(MemberDTO dto, Model model) {
		MemberDTO member = service.findPw(dto);
		if (member != null) {
			model.addAttribute("member", member);
			return "changePw";			
		} else {
			model.addAttribute("msg", "id, email 확인하세요");
			return "alert";
		}
	}
	
	@GetMapping("changePw")
	public String changePw(MemberDTO dto) {
		int row = service.changePw(dto);
		return "login";
	}
	
	@GetMapping("memberInfo")
	public void memberInfo() {
		
	}
	
	@PostMapping("memberInfo")
	public String memberInfo(MemberDTO dto, HttpSession session) {
		int row = service.modifyMember(dto);
		session.setAttribute("login", dto);
		return "redirect:/";
	}
	
	@ExceptionHandler(DuplicateKeyException.class)
	public ModelAndView duplicateUserid() {
		ModelAndView mav = new ModelAndView("alert");
		mav.addObject("msg", "이미 사용중인 ID입니다");
		return mav;
	}
}

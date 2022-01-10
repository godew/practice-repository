package com.wedog.controller;

import java.util.List;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.wedog.member.MemberDTO;
import com.wedog.service.MemberService;

@Controller
public class MemberController {
	
	@Autowired private MemberService ms;
	
	@GetMapping("memberList")
	public String memberList(Model model) {
		List<MemberDTO> members = ms.getList();
		model.addAttribute("members", members);
		return "memberList";
	}
	
	@GetMapping("login")
	public void login() {
		
	}
	
	@PostMapping("login")
	public String login(MemberDTO dto, HttpSession session, Model model) {
		MemberDTO member = ms.login(dto);
		if (member == null) {
			model.addAttribute("url", "login");
			model.addAttribute("msg", "id, pw를 확인하세요");
			return "alert";
		} else {
			session.setAttribute("login", member);
			return "redirect:/";
		}
	}
	
	@GetMapping("logout")
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/";
	}
}

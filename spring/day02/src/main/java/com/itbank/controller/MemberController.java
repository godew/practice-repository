package com.itbank.controller;

import java.io.IOException;
import java.util.List;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestHeader;

import com.itbank.model.MemberDTO;
import com.itbank.service.MemberService;

@Controller
public class MemberController {
	
	@Autowired
	private MemberService ms;
	
	@GetMapping("/join")
	public String join(Model model, HttpServletRequest req) throws IOException {
	
		String path = req.getSession().getServletContext().getRealPath("resources/agreement.txt");
		model.addAttribute("agreement", ms.getAgreement(path));
		return "join/step1";
	}
	
	@GetMapping("/join/step2")
	public String join(Model model, String agree, @RequestHeader("referer") String referer) {
		// @RequestHeader(name) = request.getHeader(name)s
		if (agree == null) {
			model.addAttribute("msg", "약관에 동의하셔야 가입이 가능합니다");
			model.addAttribute("url", referer);
			return "alert";
		}
		return "join/step2";
	}
	
	@PostMapping("/join/step3")
	public String join(MemberDTO dto, Model model) {
		int row = ms.insert(dto);
		if (row == 1) {
			return "redirect:/"; 
		} else {
			model.addAttribute("msg", "회원 가입 실패!!");
			return "alert";
		}
	}
	
	@GetMapping("/list")
	public String list(Model model) {
		List<MemberDTO> list = ms.list();
		model.addAttribute("list", list);
		return "list";
	}
}

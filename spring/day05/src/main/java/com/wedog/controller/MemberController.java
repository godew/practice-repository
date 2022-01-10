package com.wedog.controller;

import java.sql.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.wedog.member.MemberDTO;
import com.wedog.service.MemberService;

@Controller
public class MemberController {
	
	@Autowired private MemberService ms;
	
	@GetMapping("/memberList")
	public String memberList(Model model) {

		String test = ms.getTest();
		Date now = ms.getSysDate();
		model.addAttribute("test", test);
		model.addAttribute("now", now);
		
		List<MemberDTO> members = ms.getList();
		model.addAttribute("members", members);
		return "memberList";
	}
	
	@GetMapping("/memberList/{order}")
	public String memberList(Model model, @PathVariable String order) {
		
		List<MemberDTO> members = ms.findByOrder(order);
		model.addAttribute("members", members);
		return "memberList";
	}
	
	@GetMapping("/memberAdd")
	public void memberAdd() {
		
	}
	@PostMapping("/memberAdd")
	public String memberAdd(MemberDTO dto) {
		int row = ms.insert(dto);
		return "redirect:/memberList";
	}
	
	@GetMapping("/loginTest")
	public void loginTest() {}
	
	@PostMapping("/loginTest")
	public void loginTest(MemberDTO dto) {
		MemberDTO member = ms.login(dto);
		System.out.println(member == null ? "실패" : "성공");
	}
}

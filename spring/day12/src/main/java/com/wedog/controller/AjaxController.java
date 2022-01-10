package com.wedog.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.wedog.member.MemberDTO;
import com.wedog.service.MemberService;

@RestController // ajax요청을 전문적으로 처리하는 컨트롤러
				// 모든 method에 @ResponseBody 붙인다
public class AjaxController {
	
	@Autowired private MemberService memberService;
	@GetMapping("ajax1")
//	@ResponseBody // 반환하는 데이터 그대로 응답으로 보낸다.
	public String ajax1() {
		return "hello ajax!!";
		
	}
	
	@GetMapping("ajax2")
	public int ajax2(char ch) {
		return ch;
	}
	
//	@GetMapping(value="ajax3", produces = "applicatoin/json; charset=utf-8")
//	public String ajax3(String userid) throws JsonProcessingException {
//		MemberDTO member = memberService.getMember(userid);
//		ObjectMapper objectMapper = new ObjectMapper(); // java <-> js 객체 변환기
//		return objectMapper.writeValueAsString(member);
//	}
	
	@GetMapping("ajax3")
	public MemberDTO ajax3(String userid) {
		return memberService.getMember(userid);
	}
	
	@GetMapping("ajax4")
	public List<MemberDTO> ajax4() {
		return memberService.getMembers();
	}
	
	@GetMapping("ajax5")
	public List<MemberDTO> ajax5(String username) {
		return memberService.getMembersByUsername(username);
	}
	
	@GetMapping("valid")
	public boolean valid(String userid) {
		return memberService.getMember(userid) == null;
	}
}

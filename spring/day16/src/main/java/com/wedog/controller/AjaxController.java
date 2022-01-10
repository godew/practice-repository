package com.wedog.controller;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.wedog.service.MemberService;

@RestController
public class AjaxController {
	
	@Autowired private MemberService memberService;
	
	@GetMapping(value="/memberList", produces = "application/json; charset=utf-8")
	public String memberList() throws IOException {
		String data = memberService.getMemberList();
		if(data != null) {
			return data;
		}
		return "{\"message\" : \"no data\"}";
	}

}

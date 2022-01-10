package com.wedog.controller;

import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.wedog.chat.ChatComponent;

@RestController
public class AjaxController {
	
	@Autowired private ChatComponent chatComponent;
	
	@GetMapping("/list")
	public Set<String> list() {
		return chatComponent.getSessionList().keySet();
	}
}

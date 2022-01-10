package com.wedog.controller;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.wedog.service.BoardService;

@RestController
public class AjaxController {
	
	@Autowired private BoardService boardService;
	
	@GetMapping("/board/{offset}")
	public List<HashMap<String, Object>> getBoard(@PathVariable String offset) {
		return boardService.getBoard(offset);
	}
	
	@PostMapping("/board")
	public int board(@RequestBody HashMap<String, String> map) {
		return boardService.writeBoard(map);
	}
}

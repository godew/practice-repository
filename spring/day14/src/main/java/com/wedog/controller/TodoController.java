package com.wedog.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.wedog.service.TodoService;

@RestController
public class TodoController {

	@Autowired private TodoService todoService;
	
	@GetMapping("/todo")
	public List<TodoDTO> todo() {
		return todoService.findAll();
	}
	
	@PostMapping("/todo")
	public int todo(@RequestBody TodoDTO dto) {
		return todoService.join(dto);
	}
	
	@DeleteMapping("/todo/{idx}")
	public int todo(@PathVariable String idx) {
		return todoService.removeByIdx(idx);
	}
}

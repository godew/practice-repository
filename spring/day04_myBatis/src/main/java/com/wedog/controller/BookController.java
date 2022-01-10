package com.wedog.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import com.wedog.model.BookDTO;
import com.wedog.service.BookService;

@Controller
public class BookController {

	@Autowired private BookService bs;
	
	@GetMapping("/bookList")
	public String bookList(Model model) {
		List<BookDTO> books = bs.getList();
		model.addAttribute("books", books);
		return "bookList";
	}
	
	@GetMapping("/insert")
	public void insert() {
		
	}
	
	@PostMapping("/insert")
	public String insert(BookDTO dto) {
		int row = bs.add(dto);
		return "redirect:/bookList";
	}
	
	@GetMapping("/selectOne/{idx}")
	public String selectOne(@PathVariable String idx, Model model) {
		BookDTO book = bs.findByIdx(idx);
		model.addAttribute("book", book);
		return "selectOne";
	}
	
	@GetMapping("/delete/{idx}")
	public String delete(@PathVariable String idx) {
		int row = bs.remove(idx);
		return "redirect:/bookList";
	}
	
	@GetMapping("/update/{idx}")
	public String update(@PathVariable String idx, Model model) {
		BookDTO book = bs.findByIdx(idx);
		model.addAttribute("book", book);
		return "update";
	}
	
	@PostMapping("/update/{idx}")
	public String update(BookDTO dto) {
		int row = bs.modify(dto);
		return "redirect:/bookList";
	}
	
	@PostMapping("/bookList")
	public String find(Model model, String name) {
		List<BookDTO> books = bs.findByName(name);
		model.addAttribute("books", books);
		return "bookList";
	}
}

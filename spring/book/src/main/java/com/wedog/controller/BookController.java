package com.wedog.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.wedog.model.BookDTO;
import com.wedog.service.BookService;

@Controller
public class BookController {
	
	@Autowired
	private BookService bookService;
	
	@GetMapping("/insert")
	public String insert() {
		return "book/insert";
	}
	
	@PostMapping("/insert")
	public String insert(BookDTO dto) {
		bookService.addBook(dto);
		return "redirect:/list";
	}
	
	@GetMapping("/list")
	public String list(Model model) {
		List<BookDTO> list = bookService.retrieveAll();
		model.addAttribute("books", list);
		return "book/list";
	}
	
	@PostMapping("/list")
	public String list(String name, Model model) {
		List<BookDTO> list = bookService.retrieveByName(name);
		model.addAttribute("books", list);
		return "book/list"; 
	}
	
	@GetMapping("/selectOne")
	public String selectOne(int idx, Model model) {
		BookDTO book = bookService.retrieveByIdx(idx);
		model.addAttribute("book", book);
		return "book/selectOne";
	}
	
	@GetMapping("/delete")
	public String delete(int idx) {
		bookService.deleteBook(idx);
		return "redirect:/list";
	}
	
	@GetMapping("/update")
	public String update(int idx, Model model) {
		BookDTO book = bookService.retrieveByIdx(idx);
		model.addAttribute("book", book);
		return "book/update";
	}
	
	@PostMapping("/update")
	public String update(BookDTO dto) {
		bookService.updateBook(dto);
		return "redirect:/list";
	}
}

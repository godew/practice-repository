package com.wedog.controller;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.wedog.book.BookDTO;
import com.wedog.service.BookService;

@Controller
public class BookController {

	@Autowired private BookService service;
	
	@GetMapping("bookList/{order}")
	public String bookList(Model model,
						   @PathVariable String order,
						   @RequestParam HashMap<String, String> map) {
		
		map.put("order", order);
		List<BookDTO> books = service.getBooks(map);
		model.addAttribute("books", books);
		return "bookList";
	}
	
	@GetMapping("deleteBook/{idx}")
	public String deleteBook(@PathVariable String idx) {
		int row = service.deleteBook(idx);
		return "redirect:/bookList/idx";
	}
	
	@GetMapping("modifyBook/{idx}")
	public String modifyBook(@PathVariable String idx, Model model) {
		BookDTO book = service.findByIdx(idx);
		model.addAttribute("book", book);
		return "modifyBook";
	}
	
	@PostMapping("modifyBook/{idx}")
	public String modifyBook(BookDTO dto, Model model, String idx) {
		int row = service.modifyBook(dto);
		if (row == 1) {
			model.addAttribute("msg", "modify success!");
			model.addAttribute("url", "bookList/idx");
			 
		} else {
			model.addAttribute("msg", "modify fail!");
		}
		return "alert"; 
	}
	
	@GetMapping("addBook")
	public void addBook() {}
	
	@PostMapping("addBook")
	public String addBook(BookDTO dto, Model model) {
		int row = service.addBook(dto);
		if (row == 1) {
			model.addAttribute("msg", "add success!");
			model.addAttribute("url", "bookList/idx");
			 
		} else {
			model.addAttribute("msg", "add fail!");
		}
		return "alert"; 
	}
}

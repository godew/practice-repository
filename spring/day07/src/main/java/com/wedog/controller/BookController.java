package com.wedog.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import com.wedog.book.BookDTO;
import com.wedog.service.BookService;

@Controller
public class BookController {

	@Autowired private BookService service;
	
	@GetMapping("bookList/{order}")
	public String bookList(Model model, @PathVariable String order) {
		List<BookDTO> books = service.getBooks(order);
		model.addAttribute("books", books);
		return "bookList";
	}
}

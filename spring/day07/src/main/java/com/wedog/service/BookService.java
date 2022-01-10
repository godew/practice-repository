package com.wedog.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.book.BookDAO;
import com.wedog.book.BookDTO;

@Service
public class BookService {

	@Autowired private BookDAO dao;
	public List<BookDTO> getBooks(String order) {
		return dao.select(order);
	}

}

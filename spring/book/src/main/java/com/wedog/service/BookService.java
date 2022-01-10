package com.wedog.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.model.BookDAO;
import com.wedog.model.BookDTO;


@Service
public class BookService {
	
	@Autowired
	private BookDAO dao;

	public void addBook(BookDTO dto) {
		dao.insert(dto);
	}

	public List<BookDTO> retrieveAll() {
		return dao.selectAll();
	}

	public List<BookDTO> retrieveByName(String name) {
		return dao.selectByName(name);
	}

	public BookDTO retrieveByIdx(int idx) {
		return dao.selectByIdx(idx);
	}

	public void deleteBook(int idx) {
		dao.delete(idx);
	}

	public void updateBook(BookDTO dto) {
		dao.update(dto);
	}
}

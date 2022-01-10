package com.wedog.service;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.book.BookDAO;
import com.wedog.book.BookDTO;

@Service
public class BookService {

	@Autowired private BookDAO dao;
	public List<BookDTO> getBooks(HashMap<String,String> map) {
		return dao.select(map);
	}
	public int deleteBook(String idx) {
		return dao.deleteByIdx(idx);
	}
	public BookDTO findByIdx(String idx) {
		return dao.selectByIdx(idx);
	}
	public int modifyBook(BookDTO dto) {
		return dao.update(dto);
	}
	public int addBook(BookDTO dto) {
		return dao.insert(dto);
	}
}

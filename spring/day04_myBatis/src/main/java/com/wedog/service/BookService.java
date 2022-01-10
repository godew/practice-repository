package com.wedog.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.model.BookDAO;
import com.wedog.model.BookDTO;

@Service
public class BookService {

	@Autowired private BookDAO dao; 
	public List<BookDTO> getList() {
		return dao.selectAll();
	}
	public int add(BookDTO dto) {
		return dao.insert(dto);
	}
	public BookDTO findByIdx(String idx) {
		return dao.selectByIdx(idx);
	}
	public int remove(String idx) {
		return dao.deleteByIdx(idx);
	}
	public int modify(BookDTO dto) {
		return dao.update(dto);
	}
	public List<BookDTO> findByName(String name) {
		return dao.selectByName(name);
	}
}

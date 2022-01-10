package com.wedog.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.controller.TodoDTO;
import com.wedog.repository.TodoDAO;

@Service
public class TodoService {
	@Autowired private TodoDAO dao;

	public List<TodoDTO> findAll() {
		return dao.selectAll();
	}

	public int join(TodoDTO dto) {
		return dao.insert(dto);
	}

	public int removeByIdx(String idx) {
		return dao.deleteByIdx(idx);
	}
}

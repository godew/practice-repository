package com.wedog.service;

import java.util.HashMap;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.board.BoardDAO;

@Service
public class BoardService {
	
	@Autowired private BoardDAO dao;

	public List<HashMap<String, Object>> getBoard(String offset) {
		return dao.selectRange(offset);
	}

	public int writeBoard(HashMap<String, String> map) {
		return dao.insert(map);
	}
}

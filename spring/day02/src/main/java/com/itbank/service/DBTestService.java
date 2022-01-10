package com.itbank.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.itbank.model.DBTestDAO;

@Service
public class DBTestService {

	@Autowired
	private DBTestDAO dao;
	
	public String getTest() {
		return dao.selectVersion();
	}
}

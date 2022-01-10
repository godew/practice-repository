package com.wedog.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.model.TestDAO;

@Service
public class TestService {
	@Autowired private TestDAO dao;

	public String getInfo() {
		return dao.selectInfo();
	}
}

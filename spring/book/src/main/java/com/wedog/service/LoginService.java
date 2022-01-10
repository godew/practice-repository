package com.wedog.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.model.BookDTO;
import com.wedog.model.MemberDAO;
import com.wedog.model.MemberDTO;

@Service
public class LoginService {

	@Autowired
	private MemberDAO dao;
	
	public MemberDTO login(MemberDTO dto) {
		return dao.selectMember(dto);
	}
}

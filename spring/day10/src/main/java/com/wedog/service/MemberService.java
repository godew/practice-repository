package com.wedog.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.model.MemberDAO;
import com.wedog.model.MemberDTO;

@Service
public class MemberService {

	@Autowired private MemberDAO dao;
	
	public MemberDTO login(MemberDTO dto) {
		return dao.select(dto);
	}

}

package com.wedog.service;

import java.sql.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.member.MemberDAO;
import com.wedog.member.MemberDTO;
import com.wedog.member.MemberTestDAO;
import com.wedog.model.LoginDAO;

@Service
public class MemberService {
	
	@Autowired private MemberDAO dao;
	@Autowired private MemberTestDAO tdao;
	@Autowired private LoginDAO ldao;

	public String getTest() {
		return tdao.selectVersion();
	}

	public Date getSysDate() {
		return tdao.selectSysDate();
	}

	public List<MemberDTO> getList() {
		return dao.selectAll();
	}

	public List<MemberDTO> findByOrder(String order) {
		return dao.selectByOrder(order);
	}

	public int insert(MemberDTO dto) {
		return dao.insert(dto);
	}

	public MemberDTO login(MemberDTO dto) {
		return ldao.login(dto);
	}
}

package com.wedog.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.member.MemberDAO;
import com.wedog.member.MemberDTO;

@Service
public class MemberService {
	
	@Autowired private MemberDAO dao;

	public MemberDTO getMember(String userid) {
		return dao.selectByUserid(userid);
	}

	public List<MemberDTO> getMembers() {
		return dao.selectAll();
	}

	public List<MemberDTO> getMembersByUsername(String username) {
		return dao.selectByUsername(username);
	}
}

package com.wedog.service;

import java.util.List;
import java.util.UUID;
import java.util.stream.Stream;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.member.MemberDAO;
import com.wedog.member.MemberDTO;

@Service
public class MemberService {
	
	@Autowired private MemberDAO dao;

	public List<MemberDTO> getList() {
		List<MemberDTO> members = dao.selectAll();
		for (MemberDTO member : members) {
			String tmp = "";
			for (int i = 0; i < member.getUserpw().length() - 1; i++) {
				tmp += "*";
			}
			member.setUserpw(member.getUserpw().charAt(0) + tmp); 
		}
		
		return members;
	}

	public MemberDTO login(MemberDTO dto) {
		return dao.select(dto);
	}

	public int join(MemberDTO dto) {
		return dao.insertMember(dto);
	}

	public MemberDTO findPw(MemberDTO dto) {
		return dao.select(dto);
	}
	
	public int newPass(MemberDTO target) {
		String newPass = UUID.randomUUID().toString().replaceAll("-", "").substring(0, 8);
		target.setUserpw(newPass);
		int row = dao.update(target);
		return row;
	}

	public int changePw(MemberDTO dto) {
		return newPass(dao.select(dto));
	}
}

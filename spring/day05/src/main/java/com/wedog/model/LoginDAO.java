package com.wedog.model;

import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import com.wedog.member.MemberDTO;

public interface LoginDAO {

	MemberDTO login(MemberDTO dto);	
}

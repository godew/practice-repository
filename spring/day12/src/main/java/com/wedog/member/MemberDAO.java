package com.wedog.member;

import java.util.List;

import org.apache.ibatis.annotations.Select;

public interface MemberDAO {

	@Select("select * from member where userid=#{userid}")
	MemberDTO selectByUserid(String userid);

	@Select("select * from member order by userid")
	List<MemberDTO> selectAll();

	@Select("select * from member where username like '%${username}%'")
	List<MemberDTO> selectByUsername(String username);
}

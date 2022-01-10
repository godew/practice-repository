package com.wedog.member;

import java.util.List;

import org.apache.ibatis.annotations.Select;

public interface MemberDAO {

	@Select("select * from member order by userid")
	List<MemberDTO> selectAll();

	MemberDTO selectByidAndPw(MemberDTO dto);

}

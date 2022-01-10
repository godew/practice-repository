package com.wedog.model;

import org.apache.ibatis.annotations.Select;

public interface MemberDAO {

	@Select("select * from member where userid=#{userid} and userpw=#{userpw}")
	MemberDTO select(MemberDTO dto);
}

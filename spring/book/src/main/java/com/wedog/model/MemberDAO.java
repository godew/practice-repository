package com.wedog.model;

import java.sql.ResultSet;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

@Repository
public class MemberDAO {

	@Autowired
	private JdbcTemplate jt;
	
	private RowMapper<MemberDTO> rowMapper = (ResultSet rs, int rowNum) -> {
		MemberDTO dto = new MemberDTO();
		dto.setUserid(rs.getString("userid"));
		dto.setUserpw(rs.getString("userpw"));
		return dto;
	};
	
	public MemberDTO selectMember(MemberDTO dto) {
		String sql = "select * from member where userid=? and userpw=?";
		return jt.queryForObject(sql, 
				new Object[] {dto.getUserid(), dto.getUserpw()}, 
				rowMapper); 
	}
}

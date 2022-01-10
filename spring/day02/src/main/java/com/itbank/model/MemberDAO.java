package com.itbank.model;

import java.sql.ResultSet;
import java.util.List;

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
		dto.setUserid(rs.getString(1));
		dto.setUserpw(rs.getString(2));
		dto.setUsername(rs.getString(3));
		dto.setEmail(rs.getString(4));
		dto.setGender(rs.getString(5));
		return dto;
	};

	public int insert(MemberDTO dto) {
		String sql = "insert into member1 values(?, ?, ?, ?, ?)";
		return jt.update(sql, dto.getUserid(), dto.getUserpw(), dto.getUsername(), dto.getEmail(), dto.getGender());		
	}

	public List<MemberDTO> selectAll() {
		String sql = "select * from member1 order by userid";
		return jt.query(sql, rowMapper);
	}

	public MemberDTO selectMember(MemberDTO dto) {
		String sql = "select * from member1 where userid = ? and userpw = ?";
		return jt.queryForObject(sql, 
				new Object[] {dto.getUserid(), dto.getUserpw()},
				rowMapper);
	}
}

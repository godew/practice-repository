package com.itbank.model;

import java.sql.ResultSet;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

@Repository
public class DBTestDAO {
	
	@Autowired
	private JdbcTemplate jt;

	public String selectVersion() {
		String sql = "select banner from v$version";
		RowMapper<String> rowMapper = (ResultSet rs, int rowNum) -> {
			return rs.getString("banner");
		};
		
		List<String> result = jt.query(sql, rowMapper);
		return result.get(0);
	}
}

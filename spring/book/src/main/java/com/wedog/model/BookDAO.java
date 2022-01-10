package com.wedog.model;

import java.sql.ResultSet;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

@Repository
public class BookDAO {

	@Autowired
	private JdbcTemplate jt;
	
	private RowMapper<BookDTO> rowMapper = (ResultSet rs, int rowNum) -> {
		BookDTO dto = new BookDTO();
		dto.setIdx(rs.getInt(1));
		dto.setName(rs.getString(2));
		dto.setAuthor(rs.getString(3));
		dto.setPublisher(rs.getString(4));
		dto.setPublishDate(rs.getDate(5));
		dto.setPrice(rs.getInt(6));
		dto.setDescription(rs.getString(7));
		return dto;
	};
	
	public void insert(BookDTO dto) {
		String sql = "insert into book(name, "
				+ "author, "
				+ "publisher, "
				+ "publishDate, "
				+ "price, "
				+ "description) "
				+ "values(?, ?, ?, ?, ?, ?)";
		jt.update(sql,
				dto.getName(),
				dto.getAuthor(),
				dto.getPublisher(),
				dto.getPublishDate(),
				dto.getPrice(),
				dto.getDescription());
	}

	public List<BookDTO> selectAll() {
		String sql = "select * from book";
		return jt.query(sql, rowMapper); 
	}

	public List<BookDTO> selectByName(String name) {
		String sql = "select * from book where name like ?";
		return jt.query(sql, 
				new Object[] {"%" + name + "%"},
				rowMapper);
	}

	public BookDTO selectByIdx(int idx) {
		String sql = "select * from book where idx=?";
		return jt.queryForObject(sql, 
				new Object[] {idx},
				rowMapper);
	}

	public void delete(int idx) {
		String sql = "delete from book where idx=?";
		jt.update(sql, idx);
	}

	public void update(BookDTO dto) {
		String sql = "update book set "
				+ "name=?,"
				+ "author=?,"
				+ "publisher=?,"
				+ "price=?,"
				+ "description=? where idx=?";
		jt.update(sql, 
				dto.getName(),
				dto.getAuthor(),
				dto.getPublisher(),
				dto.getPrice(),
				dto.getDescription(),
				dto.getIdx());
	}
}

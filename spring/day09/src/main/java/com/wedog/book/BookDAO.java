package com.wedog.book;

import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

public interface BookDAO {

	List<BookDTO> select(HashMap<String, String> map);

	@Delete("delete from book where idx=${idx}")
	int deleteByIdx(String idx);

	@Select("select * from book where idx=${idx}")
	BookDTO selectByIdx(String idx);

	int update(BookDTO dto);

	int insert(BookDTO dto);
}

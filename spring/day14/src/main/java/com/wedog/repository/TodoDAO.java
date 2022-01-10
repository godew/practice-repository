package com.wedog.repository;

import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;

import com.wedog.controller.TodoDTO;

public interface TodoDAO {

	@Select("select * from todo order by tdate")
	List<TodoDTO> selectAll();

	@Insert("insert into todo(title, content, tdate) values(#{title}, #{content}, #{tdate})")
	int insert(TodoDTO dto);

	@Delete("delete from todo where idx=${idx}")
	int deleteByIdx(String idx);

}

package com.wedog.model;

import java.util.List;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;

public interface UploadDAO {

	@Insert("insert into image2 values(#{fileName}, #{changedName}, sysdate, #{userid})")
	int insert(UploadDTO dto);

	@Select("select * from image2")
	List<UploadDTO> selectAll();
}

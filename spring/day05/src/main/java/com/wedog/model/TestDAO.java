package com.wedog.model;

import org.apache.ibatis.annotations.Select;

public interface TestDAO {

	@Select("select banner from v$version")
	String test();
}

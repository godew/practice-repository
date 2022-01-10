package com.wedog.board;

import java.util.HashMap;
import java.util.List;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;

public interface BoardDAO {

	@Select("select idx, writer, title, content, to_char(writeDate, 'yyyy-MM-dd') as writeDate from board2\r\n" + 
			"    order by idx desc\r\n" + 
			"    offset ${offset} rows\r\n" + 
			"    fetch next 5 rows only")
	List<HashMap<String, Object>> selectRange(String offset);

	@Insert("insert into board2(title, writer, content, ipaddress) values(#{title}, #{writer}, #{content}, #{ipaddr})")
	int insert(HashMap<String, String> map);
}

package com.wedog.model;

import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.springframework.stereotype.Repository;

@Repository 
public interface BookDAO {

	@Select("select * from book order by idx")
	List<BookDTO> selectAll();

//	 #{} 는 매개변수의 getter에 접근하며, 자료형에 따라 따옴표 처리하거나 숫자이면 따옴표 붙이지 않는다.
//	 파싱된 쿼리문은 재활용(캐싱)되기 때문에 성능상 효율적
//	
//	 ${} 는 매개변수의 getter에 접근하며, 자료형에 상관없이 따옴표 처리 및 변환 없이 그대로 맵핑한다.
//	 값이 넣어진 채로 쿼리문이 수행된다. 그래서 파라미터의 값이 바뀔 때마다 항상 쿼리문 파싱을 진행해야하므로 성능상 단점이 존재
//	 #{}을 쓰는거보다 보안상 취약함 (SQL Injection)
//	
//	 특수한 경우를 제외하면, myBatis는 매개변수로 하나의 Object만 받는다
//	 여러 매개변수를 묶어서 전달하려면 HashMap을 사용할 수 있다.
	
	@Insert("insert into book values (book_seq.nextval, "
			+ "#{name}, #{author}, #{publisher}, #{publishDate}, #{price}, #{description})")
	int insert(BookDTO dto);
	
	@Select("select * from book where idx=#{idx}")
	BookDTO selectByIdx(String idx);

	@Delete("delete from book where idx=#{idx}")
	int deleteByIdx(String idx);

	@Update("update book set "
			+ "name=#{name},"
			+ "author=#{author},"
			+ "publisher=#{publisher},"
			+ "publishDate=#{publishDate},"
			+ "price=#{price},"
			+ "description=#{description} "
			+ "where idx=#{idx}")
	int update(BookDTO dto);

	@Select("select * from book where name like '%${name}%'")
	List<BookDTO> selectByName(String name);
}

package com.wedog.member;

import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class MemberDAO {
	
	@Autowired private SqlSessionTemplate sst;

	public List<MemberDTO> selectAll() {
//		sst.selectList(statement)
//		sst.selectList(statement, parameter)
//		sst.selectList(statement, parameter, rowBounds)
		return sst.selectList("selectAll");
	}

	public List<MemberDTO> selectByOrder(String order) {
		return sst.selectList("selectByOrder", order);
	}

	public int insert(MemberDTO dto) {
		return sst.insert("insert", dto);
	}
}

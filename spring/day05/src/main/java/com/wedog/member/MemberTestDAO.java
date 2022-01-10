package com.wedog.member;

import java.sql.Date;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class MemberTestDAO {
	
	@Autowired private SqlSessionTemplate sst;
	
	public String selectVersion() {
		return sst.selectOne("test1"); // test1이라는 id의 mapper 코드를 호출
	}

	public Date selectSysDate() {
		return sst.selectOne("now");
	}
}

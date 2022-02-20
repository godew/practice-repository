package com.wedog.test;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.core.env.Environment;
import org.springframework.test.context.TestPropertySource;

import static org.assertj.core.api.Assertions.*;

@SpringBootTest
@TestPropertySource(locations = "classpath:/test.properties")
class ApplicationTests {

	@Autowired
	Environment environment;

	@Test
	void contextLoads() {
		assertThat(environment.getProperty("godew.name"))
				.isEqualTo("testtest");
	}
}

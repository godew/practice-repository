package com.wedog.exam;

import org.springframework.boot.Banner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.core.env.Environment;

import java.io.PrintStream;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		SpringApplication app = new SpringApplication(Application.class);
		app.setBanner(new Banner() {
			@Override
			public void printBanner(Environment environment, Class<?> sourceClass, PrintStream out) {
				out.println("==================");
				out.println("godew Spring Boot");
				out.println("==================");
			}
		});
//		app.setBannerMode(Banner.Mode.OFF); // banner off
//		app.addListeners(new SampleListener());
		app.setWebApplicationType(WebApplicationType.NONE);
		app.run(args);
	}
}

package com.itbank.exception;

import java.io.IOException;

import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class ExceptionHandle {

	@ExceptionHandler(IOException.class)
	public String ioex(IOException e) {
		System.out.println(e);
		return "redirect:/";
	}
}

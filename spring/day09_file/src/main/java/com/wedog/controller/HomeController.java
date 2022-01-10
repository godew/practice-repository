package com.wedog.controller;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.wedog.model.UploadDTO;
import com.wedog.service.FileService;

@Controller
public class HomeController {
	
	@Autowired private FileService service;
	
	@GetMapping("upload")
	public void upload() {
		
	}
	
	@PostMapping("upload")
	public String upload(UploadDTO dto, Model model) throws IllegalStateException, IOException {
		int row = service.uploadFile(dto);
		model.addAttribute("fileName", dto.getFileName());
		return "upload";
	}
}


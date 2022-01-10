package com.wedog.controller;

import java.io.IOException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import com.wedog.model.UploadDTO;
import com.wedog.service.UploadService;

@Controller
public class HomeController {
	
	@Autowired private UploadService uploadService;
	
	@GetMapping("/")
	public String home(Model model) {
		List<UploadDTO> files = uploadService.findAll();
		model.addAttribute("files", files);
		return "home";
	}
	
	@GetMapping("upload")
	public String upload(Model model) {
		model.addAttribute("flag", "flag");
		return "home";
	}
	
	@PostMapping("upload")
	public String upload(Model model, UploadDTO dto) throws IllegalStateException, IOException {
		System.out.println("hello");
		int row = uploadService.upload(dto);
		return "redirect:/";
	}
}

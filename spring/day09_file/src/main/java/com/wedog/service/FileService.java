package com.wedog.service;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.model.UploadDAO;
import com.wedog.model.UploadDTO;

@Service
public class FileService {

	@Autowired private UploadDAO dao;
	private String upLoadPath = "D:\\upload";
	File dir;
	
	public FileService() {
		dir = new File(upLoadPath);
		if (!dir.exists()) dir.mkdir();
	}
	
	public int uploadFile(UploadDTO dto) throws IllegalStateException, IOException {
		
		String fileName = dto.getUploadFile().getOriginalFilename();
		
		// file upload
		File dest = new File(dir, fileName);
		dto.getUploadFile().transferTo(dest);
		
		dto.setFileName(fileName); // db 저장용 name
		
		return dao.insertFile(dto);
	}
}

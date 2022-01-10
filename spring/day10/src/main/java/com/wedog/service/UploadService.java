package com.wedog.service;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.wedog.model.UploadDAO;
import com.wedog.model.UploadDTO;

@Service
public class UploadService {

	private String upLoadPath = "D:\\upload";
	File dir;
	
	public UploadService() {
		dir = new File(upLoadPath);
		if (!dir.exists()) dir.mkdir();
	}

	@Autowired private UploadDAO dao;
	
	public int upload(UploadDTO dto) throws IllegalStateException, IOException {
		
		String fileName = dto.getUploadFile().getOriginalFilename();
		String changedName = UUID.randomUUID() + fileName.substring(fileName.indexOf("."));
		
		File dest = new File(dir, changedName);
		dto.getUploadFile().transferTo(dest);
		
		dto.setFileName(fileName);
		dto.setChangedName(changedName);
		
		return dao.insert(dto);
	}

	public List<UploadDTO> findAll() {
		return dao.selectAll();
	}

}

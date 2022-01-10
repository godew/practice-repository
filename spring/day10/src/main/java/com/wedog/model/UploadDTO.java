package com.wedog.model;

import org.springframework.web.multipart.MultipartFile;

public class UploadDTO {

    private String userid, fileName, changedName;
    private MultipartFile uploadFile;
	
	public String getUserid() {
		return userid;
	}
	public void setUserid(String userid) {
		this.userid = userid;
	}
	public String getFileName() {
		return fileName;
	}
	public void setFileName(String fileName) {
		this.fileName = fileName;
	}
	public String getChangedName() {
		return changedName;
	}
	public void setChangedName(String changedName) {
		this.changedName = changedName;
	}
	public MultipartFile getUploadFile() {
		return uploadFile;
	}
	public void setUploadFile(MultipartFile uploadFile) {
		this.uploadFile = uploadFile;
	}
}

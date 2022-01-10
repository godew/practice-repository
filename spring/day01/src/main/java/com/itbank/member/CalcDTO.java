package com.itbank.member;

public class CalcDTO {
	private double prev;
	private String oper;
	private double next;
	
	public double calc() {
		if (oper.equals("plus")) {
			return prev + next;
		} else if (oper.equals("minus")) {
			return prev - next;
		} else if (oper.equals("mul")) {
			return prev * next;
		} else if (oper.equals("div")) {
			if (next != 0) {
				return prev / next;				
			}
		}
		return 0;
	}

	public double getPrev() {
		return prev;
	}

	public void setPrev(double prev) {
		this.prev = prev;
	}

	public String getOper() {
		return oper;
	}

	public void setOper(String oper) {
		this.oper = oper;
	}

	public double getNext() {
		return next;
	}

	public void setNext(double next) {
		this.next = next;
	}
}

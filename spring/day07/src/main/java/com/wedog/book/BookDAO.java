package com.wedog.book;

import java.util.List;

public interface BookDAO {

	List<BookDTO> select(String order);
}

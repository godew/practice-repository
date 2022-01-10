package com.wedog.repository;

import org.apache.ibatis.annotations.Insert;

import com.wedog.controller.ImageDTO;
import com.wedog.controller.ItemDTO;
import com.wedog.controller.ItemRoomDTO;

public interface CrawlingDAO {

	@Insert("insert into item values(#{itemId},"
								  + "#{itemName},"
								  + "#{address},"
								  + "#{locale},"
								  + "#{itemPrice},"
								  + "#{itemImage},"
								  + "#{distance},"
								  + "#{latitude},"
								  + "#{longitude},"
								  + "#{filter},"
								  + "null,"
								  + "#{areaCode}"
			+ ")")
	void insertToItem(ItemDTO tmp);

	@Insert("insert into item_room values(#{itemRoomId},"
									   + "#{itemId},"
									   + "#{itemRoomName},"
									   + "#{itemRoomImage},"
									   + "#{itemRoomPrice},"
									   + "#{standardPeople},"
									   + "#{maxPeople}"
			+ ")")
	void insertToItemRoom(ItemRoomDTO tmp);

	@Insert("insert into image values(image_seq.nextval,"
								   + "#{itemRoomId},"
								   + "#{image}"
			+ ")")
	void insertToImage(ImageDTO tmp);


	@Insert("insert into calendar values(calendar_seq.nextval,"
									  + "${i}, "
									  + "cycle_seq.nextval,"
									  + "1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)")
	void insertCalendar(int i);

}

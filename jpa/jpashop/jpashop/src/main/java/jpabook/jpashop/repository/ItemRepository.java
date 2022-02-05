package jpabook.jpashop.repository;

import jpabook.jpashop.domain.item.Item;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import java.util.List;

@Repository
@RequiredArgsConstructor
public class ItemRepository {

    // @PersistenceContext 대신 @RequiredArgsConstructor 사용
    private final EntityManager em;

    public void save(Item item) {
        if(item.getId() == null) {
            em.persist(item); // 새로 생성된 item 객체를 영속성 컨텍스트에 등록
        } else {
            em.merge(item); // 이미 존재하면 update
        }
    }

    public Item findOne(Long id) {
        return em.find(Item.class, id);
    }

    public List<Item> findAll() {
        return em.createQuery("select i from Item i", Item.class)
                .getResultList();
    }
}

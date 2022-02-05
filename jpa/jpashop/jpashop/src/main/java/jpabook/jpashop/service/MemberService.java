package jpabook.jpashop.service;

import jpabook.jpashop.domain.Member;
import jpabook.jpashop.repository.MemberRepository;
import lombok.AllArgsConstructor;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional(readOnly = true) // 데이터 변경은 트랜잭션 안에서 일어나야한다. readOnly는 조회 시 성능 최적화 시켜줌
@RequiredArgsConstructor // final이 있는 필드로만 생성자를 만든다
public class MemberService {

    private final MemberRepository memberRepository;

//    @Autowired 생략 가능
//    public MemberService(MemberRepository memberRepository) {
//        this.memberRepository = memberRepository;
//    }  --> @Constructor 어노테이션으로 자동 생성

    /**
     * 회원 가입
     */
    @Transactional // readOnly = false (default) 상태, true는 읽기 전용으로 데이터 변경이 불가능함
    public Long join(Member member) {
        validateDuplicateMember(member); // 중복 회원 검증
        memberRepository.save(member);
        return member.getId(); // 영속성 컨텍스트에 저장되면(persist) key값으로 id값이 항상 존재
    }

    private void validateDuplicateMember(Member member) {
        List<Member> findMembers = memberRepository.findByName(member.getName());
        if (!findMembers.isEmpty()) {
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        }
    }

    /**
     * 회원 전체 조회
     */
    public List<Member> findMembers(){
        return memberRepository.findAll();
    }

    public Member findOne(Long memberId) {
        return memberRepository.findOne(memberId);
    }

    @Transactional
    public void update(Long id, String name) {
        Member member = memberRepository.findOne(id);
        member.setName(name);
    }
}

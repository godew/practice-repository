package com.wedog.chat;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Component;
import org.springframework.web.socket.CloseStatus;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;
import org.springframework.web.socket.handler.TextWebSocketHandler;

@Component
public class ChatComponent extends TextWebSocketHandler {
    private List<WebSocketSession> sessionList = new ArrayList<>();
    
    @Override // 연결이 성립되면(접속이 유지되면) 호출되는 함수
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {
        sessionList.add(session);
    }
 
    @Override // 메세지를 받으며 서버가 수행하는 메서드
    protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
    	System.out.println(session.getRemoteAddress());
        System.out.println(message.getPayload());
        for(WebSocketSession wss : sessionList){
            wss.sendMessage(new TextMessage(message.getPayload()));
        }
    }
 
    @Override // 연결이 종료되면 수행하는 메서드
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
    	sessionList.remove(session);
    }
}

package com.wedog.test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class SampleRunner implements ApplicationRunner {

    @Autowired
    GodewProperties godewProperties;
//    @Value("${godew.name}")
//    private String name;
//
//    @Value("${godew.age}")
//    private int age;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("=======================");
        System.out.println(godewProperties.getName());
        System.out.println(godewProperties.getAge());
        System.out.println(godewProperties.getFullname());
        System.out.println(godewProperties.getSessionTimeout());
        System.out.println("=======================");
    }
}

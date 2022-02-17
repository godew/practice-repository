package com.wedog.exam;

import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.context.event.ApplicationStartedEvent;
import org.springframework.boot.context.event.ApplicationStartingEvent;
import org.springframework.context.ApplicationListener;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

//@Component
//public class SampleListener implements ApplicationListener<ApplicationStartedEvent> {
//
//    @Override
//    public void onApplicationEvent(ApplicationStartedEvent event) {
//        System.out.println("=======================");
//        System.out.println("Application is started");
//        System.out.println("=======================");
//    }
//    @Override
//    public void onApplicationEvent(ApplicationStartingEvent event) {
//        System.out.println("=======================");
//        System.out.println("Application is starting");
//        System.out.println("=======================");
//    }
//}

//@Component
//public class SampleListener {
//
//    public SampleListener(ApplicationArguments arguments) {
//        System.out.println("foo: " + arguments.containsOption("foo"));
//        System.out.println("bar: " + arguments.containsOption("bar"));
//    }
//}

@Component
@Order(1)
public class SampleListener implements ApplicationRunner {

    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("foo: " + args.containsOption("foo"));
        System.out.println("bar: " + args.containsOption("bar"));
    }
}
package com.example.prediction;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = "com.example.prediction")
public class PredictionApplication {

    public static void main(String[] args) {
        SpringApplication.run(PredictionApplication.class, args);
    }
}
package com.example.spring_backend.dto;

import lombok.Data;

import java.util.Map;

@Data
public class PredictionRequest {

    private Map<String, Object> features;
}
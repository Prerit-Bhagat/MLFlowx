package com.example.spring_backend.controller;

import com.example.spring_backend.dto.PredictionRequest;
import com.example.spring_backend.dto.PredictionResponse;
import com.example.spring_backend.service.PredictionService;

import lombok.RequiredArgsConstructor;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
public class PredictionController {

    private final PredictionService predictionService;

    @GetMapping("/health")
    public String health() {

        return "Backend Running";
    }

    @PostMapping("/predict")
    public PredictionResponse predict(
            @RequestBody PredictionRequest request
    ) throws Exception {

        return predictionService.predict(request);
    }
}
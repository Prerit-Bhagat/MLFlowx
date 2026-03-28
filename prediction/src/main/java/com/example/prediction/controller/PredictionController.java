package com.example.prediction.controller;

import com.example.prediction.model.PredictionRequest;
import com.example.prediction.model.PredictionResponse;
import com.example.prediction.service.PredictionService;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/predict")
public class PredictionController {

    private final PredictionService service;

    public PredictionController(PredictionService service) {
        this.service = service;
    }

    @PostMapping
    public PredictionResponse predict(@RequestBody PredictionRequest request) {
        return service.predict(request);
    }
}
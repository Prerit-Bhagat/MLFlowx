package com.example.prediction.client;

import com.example.prediction.model.PredictionRequest;
import org.springframework.stereotype.Component;

@Component
public class MLClient {

    // 🔥 Temporary logic (replace with Flask later)
    public int getPrediction(PredictionRequest request) {
        // Dummy logic for now
        return request.getYear() * 10 - request.getKmDriven() / 100;
    }
}
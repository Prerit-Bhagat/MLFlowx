package com.example.prediction.service;

import com.example.prediction.client.MLClient;
import com.example.prediction.entity.PredictionEntity;
import com.example.prediction.model.PredictionRequest;
import com.example.prediction.model.PredictionResponse;
import com.example.prediction.repository.PredictionRepository;

import org.springframework.stereotype.Service;

@Service
public class PredictionService {

    private final PredictionRepository repository;
    private final MLClient mlClient;

    public PredictionService(PredictionRepository repository, MLClient mlClient) {
        this.repository = repository;
        this.mlClient = mlClient;
    }

    public PredictionResponse predict(PredictionRequest request) {

        // 🔥 Step 1: Call ML service (for now dummy fallback)
        int prediction = mlClient.getPrediction(request);

        // 🔥 Step 2: Save to DB
        PredictionEntity entity = new PredictionEntity();
        entity.setYear(request.getYear());
        entity.setKmDriven(request.getKmDriven());
        entity.setPrediction(prediction);

        repository.save(entity);

        // 🔥 Step 3: Return response
        PredictionResponse response = new PredictionResponse();
        response.setPrediction(prediction);

        return response;
    }
}
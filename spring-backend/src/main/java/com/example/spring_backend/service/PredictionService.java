package com.example.spring_backend.service;

import com.example.spring_backend.dto.PredictionRequest;
import com.example.spring_backend.dto.PredictionResponse;
import com.example.spring_backend.entity.PredictionHistory;
import com.example.spring_backend.repository.PredictionHistoryRepository;

import com.fasterxml.jackson.databind.ObjectMapper;

import lombok.RequiredArgsConstructor;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.time.LocalDateTime;

@Service
@RequiredArgsConstructor
public class PredictionService {

    private final RestTemplate restTemplate;

    private final PredictionHistoryRepository repository;

    @Value("${inference.service.url}")
    private String inferenceServiceUrl;

    public PredictionResponse predict(
            PredictionRequest request
    ) throws Exception {

        HttpHeaders headers = new HttpHeaders();

        headers.setContentType(
                MediaType.APPLICATION_JSON
        );

        HttpEntity<Object> entity =
                new HttpEntity<>(
                        request.getFeatures(),
                        headers
                );

        ResponseEntity<PredictionResponse> response =
                restTemplate.exchange(
                        inferenceServiceUrl + "/predict",
                        HttpMethod.POST,
                        entity,
                        PredictionResponse.class
                );

        PredictionResponse prediction =
                response.getBody();

        ObjectMapper mapper = new ObjectMapper();

        PredictionHistory history =
                PredictionHistory.builder()
                        .inputData(
                                mapper.writeValueAsString(
                                        request.getFeatures()
                                )
                        )
                        .prediction(
                                prediction.getPrediction()
                        )
                        .createdAt(
                                LocalDateTime.now()
                        )
                        .build();

        repository.save(history);

        return prediction;
    }
}